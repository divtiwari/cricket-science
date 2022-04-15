function [mean, sd] = berex(avg,r,balls)
%BEREX Return the average and std dev of the Bernoulli Run Expectation
%for a player
%   avg: Average, r: score/concede rate; this is either SR/100 or Econ/6,
%   balls: Total number of balls in innings
% Dependencies: Statistics & Machine Learning Toolbox (for binopdf)

p = r/avg;    %Prob of dismissed
%Adjust r to be actual scoring rate
r = r/(1-p);

wickets = 10;   %TEMP, will make it a defaulted parameter

Eout = 0;
Eover = 0;
Eoutsq = 0;
Eoversq = 0;
for b = wickets:balls
    Eout = Eout + r*(b - wickets)*binopdf(wickets-1,b-1,p)*p;
    Eoutsq = Eoutsq + (r^2)*((b - wickets)^2)*binopdf(wickets-1,b-1,p)*p;
end
for w = 0:wickets-1
    Eover = Eover + r*(balls - w)*binopdf(w,balls,p);
    Eoversq = Eoversq + (r^2)*((balls - w)^2)*binopdf(w,balls,p);
end

mean = Eout + Eover;
sd = sqrt(Eoutsq + Eoversq - mean^2);

end