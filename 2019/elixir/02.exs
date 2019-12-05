#! /usr/bin/env elixir

defmodule Day02 do
  def run(intcode, action\\1, index\\0) 
  def run(c, 1, i), do: run_op(c, i, &+/2)
  def run(c, 2, i), do: run_op(c, i, &*/2)
  def run(c, 99, _), do: c[0]

  defp run_op(c, i, op) do
    Map.put(c, c[i+3], op.(c[c[i+1]], c[c[i+2]]))
      |> (&(run(&1, &1[i+4], i+4))).()
  end

  def find(intcode, search) do
    for noun <- 0..100,
        verb <- 0..100,
        run(%{intcode | 1 => noun, 2 => verb}) == search,
        do: 100 * noun + verb
  end
end

intcode = File.read!("../input/02")
  |> String.trim_trailing
  |> String.split(",")
  |> Enum.map(&String.to_integer/1)
  |> Enum.with_index 
  |> Enum.map(fn {k,v} -> {v,k} end) 
  |> Map.new

intcode 
  |> Map.put(1, 12)
  |> Map.put(2, 2)
  |> Day02.run
  |> IO.inspect(label: "Part 1")

intcode 
  |> Day02.find(19690720)
  |> IO.inspect(label: "Part 1")

