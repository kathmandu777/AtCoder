input=gets.chomp

alphas=[*"a".."z"] 
# I knew how to make array like this

bool=false


#remember how to use each sentence
alphas.each do |alpha|
    if bool==true
        puts alpha
        break
    end

    if alpha==input
        bool=true
    end

end
