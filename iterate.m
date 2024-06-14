function exp = iterate(inp)
    expr = str2sym(inp);
    x = symvar(expr);
    J = jacobian(expr, x)
    exp = x - mtimes(expr,J^(-1));
end