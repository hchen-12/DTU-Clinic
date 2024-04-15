%% this generates the rtc files (structs of all the data for a simulation rtc file seen in pdap). change filename to simulation hdf5 file.
%% right click and save as the rtc variable from workspace after. Then run clinicpost2.m on those saved rtc.mat files
%% peyton teneyck peytoniteneyck@gmail.com (4/15/24)

clc
clear

filename = "C:\Users\peyto\Downloads\wsp3_htc4.hdf5";
info = h5info(filename)
groups = info.Groups
g = {};
for i = 1:length(groups)
    g{i} = groups(i).Name;
end

bea3angle =[];
bea3angle_speed = [];
WSPVx=[];
WSPVy = [];
WSPVz=[];
w = [];
AeThrust = [];
AeTorque = [];
AePower = [];
IFy1 = [];
IFy2 = [];
IFy3 = [];
fx = [];
fy=[];
fz=[];
Mx=[];
My=[];
Mz=[];

for i = 1:length(g)
group = g{i};
str = append(group,'/data');
data = h5read(filename, str );
bea3angle(end+1) =data(1);
bea3angle_speed(end+1) = data(2);
WSPVx(end+1)=data(3);
WSPVy(end+1) = data(4);
WSPVz(end+1)=data(5);
w(end+1) = data(6);
AeThrust(end+1) = data(7);
AeTorque(end+1) = data(8);
AePower(end+1) = data(9);
IFy1(end+1) = data(10);
IFy2(end+1) = data(11);
IFy3(end+1) = data(12);
fx(end+1) = data(13);
fy(end+1)=data(14);
fz(end+1)=data(15);
Mx(end+1)=data(16);
My(end+1)=data(17);
Mz(end+1)=data(18);
end

rtc4 = struct('bea3angle',bea3angle,'bea3angle_speed',bea3angle_speed,'WSPVx',WSPVx,'WSPVy',WSPVy,'WSPVz',WSPVz,'w',w,'AeThrust',AeThrust,'AeTorque',AeTorque,'AePower',AePower,'IFy1',IFy1,'IFy2',IFy2,'IFy3',IFy3,'fx',fx,'fy',fy,'fz',fz,'Mx',Mx,'My',My,'Mz',Mz);
