function ret = calc(f,x)
    ret = double(subs(f,symvar(f),x));
end