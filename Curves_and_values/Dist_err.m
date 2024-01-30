clear all;
close all;

function [x, y] = trilateration(x1, y1, r1, x2, y2, r2, x3, y3, r3)
  A = 2*[x2 - x1, y2 - y1; x3 - x1, y3 - y1]
  b = [r1^2 - r2^2 + x2^2 - x1^2 + y2^2 - y1^2; r1^2 - r3^2 + x3^2 - x1^2 + y3^2 - y1^2]
  result = A \ b
  x = result(1);
  y = result(2);
end



x1 = 85;
y1 = 70;
r1 = 117;

x2 = 200;
y2 = 70;
r2 = 15;

x3 = 140;
y3 = 185;
r3 = 162;

[x, y] = trilateration(x1, y1, r1, x2, y2, r2, x3, y3, r3);
disp(['Position estimée : (', num2str(x), ', ', num2str(y), ')']);
