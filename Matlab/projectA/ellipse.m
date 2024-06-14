function [x,y] = ellipse(a,b,n)
%Exercise A1
    %Generate equally spaced points along the ellipse
    t = linspace(0*2*pi/n,2*pi,n);
    x = a.*cos(t);
    y = b.*sin(t);
end