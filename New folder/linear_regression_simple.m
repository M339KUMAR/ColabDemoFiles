%% Linear Regression Example
% This is an example for linear regression using simple data

%% Set Parameters
% Set the learning rate and stopping criterion
alp = 0.1; %Learning rate
ep = 1.e-3; %Stopping tolerance, try 1.e-6

%% Data Generation
% Data was generated synthetically by taking linear data and adding noise to it.
m = 51;
x = linspace(0,1,m);
y = 15*x + 5 + normrnd(0,0.4,size(x));  %Add Gaussian noise to original function

%% Visualize the raw Data
% Plot the data
plot(x,y,'o');

%% Make initial guesses for w
% We will make random guesses for  
w1 = rand(1); w0 = rand(1); %Random guesses

%% Iterating for w using gradient descent
% We now perform gradient descent on w = [w0, w1] in order to improve w
J(1) = 0.5/m*sum((y-w1*x-w0).^2); %Initial value of J -- the cost function

%% err is a variable which denotes the appropriate error variable which we wish to control. 
% The stopping criterion we will use is 
% We have two choices for stopping crtieria
err = 1; 
iter = 1;

while(err>ep) %Run if stopping criterion is not satisfied
    % The hypothesis function is 
    yh = w1*x + w0;
    
    % The gradient has two components
    DJ0 = (yh-y); 
    dw0 = -alp*sum(DJ0)/m;
    DJ1 = (yh-y).*x; 
    dw1 = -alp*sum(DJ1)/m;
    
    w0 = w0  + dw0;
    w1 = w1 + dw1;
    
    iter = iter + 1;

    J(iter) = 0.5/m*sum((y-w1*x-w0).^2);
    err = abs(J(iter)-J(iter-1));
    %err = norm([dw0,dw1]);   
    
    %  Create Plots
    subplot(211)
    plot(x,y,'o',x,yh,'r');
    xlabel('x')
    ylabel('y')
    legend({'Data','Linear Fit'},'Location', 'NorthWest')
    drawnow;
    subplot(212)
    plot([1:iter],J([1:iter]),'-o');
    xlabel('iterations');
    ylabel('J')
    drawnow;
    
end