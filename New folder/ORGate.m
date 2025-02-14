clear; close all;

x = [0 0;0 1; 1 0; 1 1];
y = [0 ; 1 ; 1 ; 1];
alp = 1 ; ep = 1.e-3;
w = LogisticModel(x, y, alp, ep);