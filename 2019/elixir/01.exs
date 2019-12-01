#! /usr/bin/env elixir

defmodule Day01 do
  def fuel(mass), do: Integer.floor_div(mass, 3) - 2
  def recursive_fuel(mass, acc\\0) do
    case fuel(mass) do
        x when x <= 0 -> acc
        next -> recursive_fuel(next, acc+next)
    end
  end
end


masses = File.stream!("../input/01")
  |> Stream.map(&String.trim_trailing/1)
  |> Enum.map(&String.to_integer/1)

masses 
  |> Enum.map(&Day01.fuel/1) 
  |> Enum.sum 
  |> IO.inspect(label: "Part 1")
masses 
  |> Enum.map(&Day01.recursive_fuel/1) 
  |> Enum.sum 
  |> IO.inspect(label: "Part 2")
