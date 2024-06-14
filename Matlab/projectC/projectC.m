%% Project C - random matrix spectra
% Candidate number 1045139

%% Exercise C1
type RandSpec.m
%Obtain Eigenvalues
EigenValues = RandSpec(800);
%Plot them on a histrogram with 100 bins
hold off;
histogram(EigenValues, 100)
%Add axis titles, etc.
title("Exercise C1 histogram")
xlabel("Eigenvalue value")
ylabel("Number")
%This histogram looks fairly close to an ellipse with some noise, or
%perhaps a truncated gaussian distribution.
%% Exercise C2
type MaxEval.m
%Define an X range
X = 1:800;
%Obtain values from MaxEval
Y = MaxEval(800);
%Plot the values of Y(i) and the values of 2.8sqrt(i) on the same plot
plot(X,Y)
hold on;
plot(X,2.8.*X.^(.5))

%Add a legend, axis titles, etc.
l = legend("Generated Values","$y=2.8\sqrt{x}$");
title("Exercise C2 histogram")
xlabel("x")
ylabel("y")
%Set legend interpreter to latex
set(l, "interpreter", "latex")
hold off;
%% Exercise C3
%Generate Eigenvalues of a 1000x1000 matrix
EigenValues = RandSpec(1000);
%Plot it's histogram, as in C1
histogram(EigenValues, 100)

%The highest bar appears to be at 14. Initialize a and b
b = 14;
a = 2.8*1000^.5;
%Plot the upper half of the ellipse (x/a)^2 + (y/b)^2 = 1 on the same
%graph, i.e. plotting y = b*sqrt(1 - (x/a)^2) for x in [-a, a] 
hold on;
fplot(@(x) b*(1-(x/a)^2)^.5,[-a,a]);
%Add legend, axis titles, etc.
legend("Eigenvalues", "Ellipse")
xlabel("Eigenvalue value")
ylabel("Number")
%The graph looks better approximated by b=13 but aside from that it
%the histogram is reasonably bounded by the given ellipse.