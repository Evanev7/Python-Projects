function [len] = arclength(x,y)
%Exercise A2
    %Get n, the number of elements of each of the input sets
    n = length(x);
    %Initialize the length
    len = 0;
    %Iterate from 1 to n-1
    for i = 1:(n-1)
        %Calculate the length of the sides of each sector
        xdiff = x(i+1) - x(i);
        ydiff = y(i+1) - y(i);
        %Add the hypotenuse of each sector to len
        len = len + sqrt(xdiff.^2 + ydiff.^2);
    end
end