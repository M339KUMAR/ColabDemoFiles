function w = LinModel(x, y, alp, ep)

[m,n] = size(x);
w = rand(n+1,1);
for i = 1:m
    yh(i,1) = [1 x(i,:)]*w; %[1 x] is augmenting x with x0 = 1 to acheive the multiplication
end

J(1) = 0.5/m*sum((y-yh).^2); %Initial value of J -- the cost function

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
        yh(i,1) = [1 x(i,:)]*w; %[1 x] is augmenting x with x0 = 1 to acheive the multiplication
    end
    iter = iter + 1;

    J(iter) = 0.5/m*sum((y-yh).^2);
    %err = abs(J(iter)-J(iter-1));
    err = norm(alp*DJ);   
    
    subplot(211)
    plot(x(:,1),y,'o',x(:,1),yh,'r');
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
