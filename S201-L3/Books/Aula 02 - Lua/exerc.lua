-- Exercicio 01
dofile("garbage.lua")
function tabuada(n)
  for i=0,10 do
    print(n.." x "..i.." = "..n*i)
  end
end

local x = io.read()
tabuada(x)


-- Exercicio 02
local pares = 0
local a = {}
for i=0,100 do
  a[i] = math.random(0,100)
end

for i in pairs(a) do
  if a[i]%2 == 0 then
    pares = pares + 1
  end
end

print(pares.." pares na table")