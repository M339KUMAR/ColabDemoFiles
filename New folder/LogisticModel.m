%This is the same as the GeneralizedLogisticRegression file without the comments
function w = LogisticModel(x, y, alp, ep)

[m,n] = size(x);
w = rand(n+1,1);

sigmoid = @(z) 1./(1+exp(-z));
for i = 1:m
    z = [1 x(i,:)]*w; %[1 x] is augmenting x with x0 = 1 to acheive the multiplication
    yh(i,1) = sigmoid(z);
end

J(1) = -1*sum(y.*log(yh)+(1.-y).*log(1.-yh)); %Initial value of J -- the cost function

err = 1; 
iter = 1;

while(err>ep) %Run if stopping criterion is not satisfied
    pred_err = yh - y;
    DJ(1,1) = sum(pred_err)/m;
    for j = 2:n+1
        DJ(j,1) = sum(pred_err.*x(:,j-1))/m;
    end
  
    w = w - alp*DJ;
 
    for i = 1:m
        z = [1 x(i,:)]*w; %[1 x] is augmenting x with x0 = 1 to achieve the multiplication
        yh(i,1) = sigmoid(z); 
    end
    iter = iter + 1;

    J(iter) = -1*sum(y.*log(yh)+(1.-y).*log(1.-yh));
    err = abs(J(iter)-J(iter-1));
    %err = norm(alp*DJ);   
    
    subplot(211)
    hp = [0 -w(1)/w(3);1 -(w(1)+w(2))/w(3)];
    plot(x(:,1),x(:,2),'o',hp(:,1),hp(:,2),'r'); 

    xlabel('x')
    ylabel('y')
    legend({'Data','Classifying Line'},'Location', 'NorthWest')
    drawnow;
    
    subplot(212)
    plot([1:iter],J([1:iter]),'-o');
    xlabel('iterations');
    ylabel('J')
    drawnow;
    
end
