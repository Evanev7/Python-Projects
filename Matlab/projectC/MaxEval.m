function e = MaxEval(n)
% Exercise C2
    %Preallocate e's size for reduced memory usage
    e = zeros(n,1);
    %Iterate across i in {1,...,n}
    for i = 1:n
        %Generate Eigenvalues from an ixi matrix
        EigenValues = RandSpec(i);
        %Store the maximum element of EigenValues in e(i)
        e(i) = max(EigenValues);
    end
end