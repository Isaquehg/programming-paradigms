module Main where
-- Commments
a = [1,2,3]

reverseFunc = product ((reverse (a ++ [4,5,6,7])), 5)

func n
    | n > 0 = fatorial n
    | otherwise = n * 2

fatorial :: Int -> Int
fatorial n =
    if n == 1 then 1
    else n * fatorial n - 1

main = do
    putStrLn "Haskell Classes"
    text <- getLine  
    putStrLn ("Promped Text: " ++ text) 

    n <- getLine
    print(func (read n :: Int))
    
    print(reverseFunc)

    print(fatorial 1)
    print(fatorial 5)