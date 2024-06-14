function e = RandSpec(n)
% Exercise C1
    %Generate M, an nxn matrix of Gaussian variables
    M = randn(n);
    %Symmetrise it to produce S
    S = M + M.';
    %Output the eigenvalues of S
    e = eig(S);
end