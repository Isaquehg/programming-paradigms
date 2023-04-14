-- Variavel local
x=2
do
 local x = 10
 print(x)
end

-- Print
print(x)

-- Leitura
x=io.read()
print()
print(x.." => "..type(x))

-- Casting
y = "3"
y = tonumber(y)
print(y*2)

-- Table
a = {}
a["x"] = 2;
print(a.x)
a[0] = 3;
print(a[0])

-- If (decisao)
if a["x"] <= 2 then
  print("menor ou igual")
else
  print("maior")
end

-- While (repeticao)
i=0
while i<4 do
  print(i)
  i = i+1
end

-- For (repeticao)
for i=0,10,2 do
  print(i)
end

-- Repeat (repeticao)
repeat
  print("oi")
  local linha = io.read()
until linha ~= "ficar"

-- Function
local function somaArray (a)
  local sum = 0
  for i,v in pairs(a) do --[[ iterando o array 
    (pairs retorna um iterator de pares chave(i)-valor(v))]]
    print(i," ",v)
    sum = sum + v
  end
  return sum
end

-- Exercicios
dofile("exerc.lua")