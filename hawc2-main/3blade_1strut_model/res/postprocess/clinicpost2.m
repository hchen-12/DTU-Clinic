%% run after running clinicpost.m
clear
clc

rtc0 = load("rtc0.mat");
rtc1 = load("rtc1.mat");
rtc2 = load("rtc2.mat");
rtc3 = load("rtc3.mat");
rtc4 = load("rtc4.mat");

R = 0.75; %m
rho = 1.204; %kg/m^3
H = 6/3.2808399; %m
A = (R*2)*H; %m^2

TSR0 =[];
TSR1 =[];
TSR2 =[];
TSR3 =[];
TSR4 =[];

cp0 =[];
cp1 =[];
cp2 =[];
cp3 =[];
cp4 =[];

for i = 1:length(rtc0.rtc0.w(:))
    TSR0(end+1)= (rtc0.rtc0.w(i))*R/rtc0.rtc0.WSPVy(i);
    TSR1(end+1) = (rtc1.rtc1.w(i))*R/rtc1.rtc1.WSPVy(i);
    TSR2(end+1) = (rtc2.rtc2.w(i))*R/rtc2.rtc2.WSPVy(i);
    TSR3(end+1) = (rtc3.rtc3.w(i))*R/rtc3.rtc3.WSPVy(i);
    TSR4(end+1) = (rtc4.rtc4.w(i))*R/rtc4.rtc4.WSPVy(i);
    
    cp0(end+1) = (rtc0.rtc0.AePower(i))/(0.5*rho*A*((rtc0.rtc0.WSPVy(i))^3));
    cp1(end+1) = (rtc1.rtc1.AePower(i))/(0.5*rho*A*((rtc1.rtc1.WSPVy(i))^3));
    cp2(end+1) = (rtc2.rtc2.AePower(i))/(0.5*rho*A*((rtc2.rtc2.WSPVy(i))^3));
    cp3(end+1) = (rtc3.rtc3.AePower(i))/((0.5*rho*A*(rtc3.rtc3.WSPVy(i))^3));
    cp4(end+1) = (rtc4.rtc4.AePower(i))/((0.5*rho*A*(rtc4.rtc4.WSPVy(i))^3));
end

figure(1)
clf
plot(TSR0,cp0)
grid on
hold on
plot(TSR1,cp1)
plot(TSR2,cp2)
plot(TSR3,cp3)
plot(TSR4,cp4)
xlabel("TSR")
ylabel("Cp")
legend("rtc0","rtc1","rtc2","rtc3","rtc4")
title("Cp vs TSR")
