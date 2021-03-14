#practice ruby

h,a=gets.chomp.split.map(&:to_i)
count=0

# I learned how to write "while"
while h>0 do
    h-=a      # Can not Increment and Decrement
    count+=1
end

puts count










