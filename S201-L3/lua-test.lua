-- Exercício 1
num = io.read()
local function tabuada (num)
    for i = 0, 10 do
        print(i * num)
    end
end
tabuada(num)

-- Exercício 2
a = {}
for j = 1, 100 do
    a[j] = math.random(1, 100)
    if a[j] % 2 == 0 then
        print(a[j])
    end
end