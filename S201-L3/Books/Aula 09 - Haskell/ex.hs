module Main where

func x:
    | x == 1 = 1
    | x == 0 = 0
    | otherwise = sum(x * x - 1)

func n:
    | n > 0 = fatorial n
    | otherwise = n * 2

main = do
    n <- getLine
    func :: n