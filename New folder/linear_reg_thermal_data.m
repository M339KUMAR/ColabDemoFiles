%% example for need of data normalization
% model 'LinModel.m' will be required 
clear; close all;

T = [80:-20:-340];
Talp = [6.47 6.36 6.24 6.12 6.00 ...
    5.86 5.72 5.58 5.43 5.28 5.09 ...
    4.91 4.72 4.52 4.3 4.08 3.83 ...
    3.58 3.33 3.07 2.76 2.45];
Talp = Talp*1e-6;

x = T';
y = Talp';

%% Check the Linear coeffs first
alp = 0.1; 
ep = 1.e-5;

%% 'LinModel.m' will be called here
w = LinModel(x,y,alp,ep); 

%% Let us try with rescaling of data
% comment line 20 and un-comment line 24-26
%xn = (x-min(x))/(max(x)-min(x));
%yn = y;
%w = LinModel(xn, yn, alp, ep);

%% Quadratic with rescaling
% for this un-comment line 29-30, and comment line 21 and 25
% X2 = [xn xn.^2 xn.^3]; 
% w = LinModel(X2, yn, alp, ep);