% Total time for an occluded vision+Estimation+VerbalReport Tiral
% (27,000ms)
% 1. aiming and Visual status warning (1,000ms)
% 2. Target presentation (6,000ms): 
                        % Warning to shoot after the first beep (1,000)
                        % Initiation of Vision Occlusion (1,000ms)
                        % Beep 1 (500ms)
                        % Triggering time (2,000ms)
                        % Termination of Vision Occlusion (1,000ms)
                        % Beep 2 (500ms)
% 3. Estimation warning (1,000ms)
% 4. Estimation (3,000ms)
% 5. Verbal report warning (1,000ms)
% 6. Verbal report (15,000ms)

% Estimation Verbal Report
% Occluded trial



% codes

% 1 aim1 beep
% 2 glasses occluded
% 3 glasses open
% 4 fire beep
% 5 accuracy received Verbal
% 6 accuracy received Estimate
% 7 accuracy received Basic
% 10 target appears 7y
% 15 target appears 15y
% 50 trigger pull
% 250 experiment start


function EDASI_Trials

InitializePsychSound();
initCom;
LoadPsychHID;
commandwindow;


global w aftershottime deadline distcode cleartime wavedata pahandle inst1time targtex aimtime2 isoccluded aimtime margin y resttime linespace pretrialtime
global date subjectnum subname centery ioObj sObj dataFile ExpStart 
% durations
inst1time = 1;
aimtime = 2;
aimtime2 = 1.25;
pretrialtime = 1;
resttime = 3;
cleartime = .01;
deadline = 30;
aftershottime = 1;

recordeeg = 1;

% number of each type of trial in each block
numbasic = 10;
numvrep = 2;
numest = 2;

basictrials = ones(1,numbasic);
x = ones(1,numvrep);
vreptrials = x*2;
x = ones(1,numest);
esttrials = x*3;

% we will shuffle this array to get our trial order for each block
trialtypes = [basictrials vreptrials esttrials];

% counterbalanced occulsion block orders
% 1 = occluded
% 0 = unoccluded
occorders = [1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0;
    0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 ;
    1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 ;
    0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 ];

% counterbalanced distance orders
% 1 = 13.716 meters,15 yards
% 0 = 6.401 meters, 7 yards

% THIS VARIABLE IS NOW MEANINGLESS. THERE IS ONLY ONE DISTANCE
distorders = [1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0;
    0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1;
    0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1;
    1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0];

% easy way to decide which orders each subject gets
whichorder = [1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 ...
    1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 ...
    1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 ...
    1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4];

repeat=1;
while (repeat)
    prompt={'sub initials','sub number','date'}; % expnumber indexes the stimlists and determines boundary rotation and starting boundary
    defaults={'DELETEME', '1', 'enter date'};
    answer=inputdlg(prompt,'Run experiment',1,defaults);
    [subname, subjectnum, date]=deal(answer{:});
    subint = str2double(subjectnum);

    dfileName = ['data\EDASI' subjectnum  '_' subname '.dat'];
    if exist(dfileName)~=0
        button=questdlg(['Overwrite data\EDASI' subjectnum  '_' subname '.dat?']);
        if strcmp(button,'Yes'); repeat=0; end
    else
        repeat=0;
    end

end

dataFile = fopen(dfileName, 'w');

fprintf(dataFile,'subname\tsubnum\tdate\tdistance\toccluded\ttrialtype\tRT\tAC\ttimestamp\n');

% initialize random number generator
rand('twister',str2double(subint));

% use subject number to determine the order of occlusion and distance
% blocks
myblockorder = whichorder(subint);
myoccorder = occorders(myblockorder,:);
mydistorder = distorders(myblockorder,:);

junkrect = [0 0 500 500];
pahandle = PsychPortAudio('Open', [], [], 0);
Screen('Preference','SkipSyncTests', 1);
Screens = Screen('Screens');
%whichscreen = max(Screens);

%FOR DEBUGGING
%[w, wRect] = Screen('OpenWindow', whichscreen,[], junkrect);

% FOR REAL EXPERIMENT
[w, wRect] = Screen('OpenWindow', 2);
[centerx,centery] = RectCenter(wRect);	
linespace = 15;
margin = 200;

Screen('TextSize', w, 30);
Screen('TextFont', w, 'Arials');
Screen ('TextStyle', w, 1);
mytext1 = 'Aim after the first BEEP';
mytext2 = 'Fire when ready after the second BEEP, but do not rush';
mytext3 = 'In some trials your vision after the first BEEP will be occluded';
mytext4 = 'When trial is completed, stay relaxed and calm for the next trial';
   
%scale = 1;
myimgfile='5mBBTarget_NRAAR-4_4.5mm_5.5.jpg'; %real target: 17 by 17 cm (6.7 by 6.7 in)  Bulls Eye ø59.5 mm 
img=imread(myimgfile, 'jpg');
%img2 = imresize(scale,img);
tex7yards = Screen('Maketexture', w, img); 

%myimgfile='5m BB Target NRA AR-4-10_4.5 mm.jpg'; % .754" bull
%img=imread(myimgfile, 'jpg');
%tex15yards = Screen('Maketexture', w, img); 

wavfilename = ('Censored_Beep.wav');
[y, ~] = audioread(wavfilename);
wavedata = y';


if recordeeg
    % Initialize port, set to 0
    ioObj = io64;
    status = io64(ioObj);
    %address = hex2dec('378');
    io64(ioObj,888,0);
end

ExpStart = GetSecs;
io64(ioObj,888,250);
WaitSecs(0.005);
io64(ioObj,888,0);
for blocki = 1:numel(myoccorder)
    
    
    
    PLATO_trial(1); % open glasses
    
    isoccluded = myoccorder(blocki);
    
    if mydistorder(blocki) == 1 %15 yards block
        targtex = tex7yards;
        distcode = 10;
    else % 7 yards block
        targtex = tex7yards;
        distcode = 10;
    end    
    
    if blocki == 1
        Screen('DrawText',w,mytext1,margin,centery);
        Screen('Flip',w);
        WaitSecs(3);
        Screen('DrawText',w,mytext2,margin,centery);
        Screen('Flip',w);
        WaitSecs(4);
        %if isoccluded
            Screen('DrawText',w,mytext3,margin,centery);
            %WaitSecs(inst1time);
        %end
        Screen('Flip',w);
        WaitSecs(4);
        Screen('DrawText',w,mytext4,margin,centery);
        Screen('Flip',w);
        WaitSecs(5);
        
        Screen('DrawText',w,'Experimenter will advance when you are ready',margin,centery);
        %Screen('DrawText',w,'(Experimenter, press a key to advance)',margin,centery+100);
        Screen('Flip',w);
        KbStrokeWait;
    else
        
        Screen('DrawText',w,'Next block, experimenter will advance when you are ready',margin,centery);
        Screen('DrawText',w,'(Experimenter, press a key to advance)',margin,centery+100);
        Screen('Flip',w);
        KbStrokeWait;
        
    end
    
   
    PLATO_trial(0);
    
    trialorder = Shuffle(trialtypes);
    for triali = 1:numel(trialorder)
        
        PLATO_trial(1); % open glasses
        
        trialtype = trialorder(triali);
       
        if trialtype == 1 %basic trials
            Basic();
        elseif trialtype == 2 % verbal report trials
            VerbalRep(blocki,triali);
        elseif trialtype == 3 % estimation trials
            Estimate();
        end
        
        Screen('Flip',w);  % turn target off
        
        
    end
    
end
fclose(sObj); %make sure you close the serial port at the end
Screen('DrawText',w,'END OF EXPERIMENT',margin,centery);
Screen('DrawText',w,'(PRESS ANY KEY TO EXIT)',margin,centery+100);
Screen('Flip',w);
KbStrokeWait;
clear all
Screen('Close');
Screen('CloseAll');



function VerbalRep(blocki,triali)
%Estimation Verbal Report
global w aftershottime wavedata pahandle targtex isoccluded aimtime aimtime2 pretrialtime resttime cleartime distcode deadline
global date subjectnum subname centery ioObj sObj dataFile margin TrialStart ExpStart

Screen('DrawTexture', w, targtex);
targtime = Screen('Flip',w); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, distcode); WaitSecs(cleartime); lptwrite(888, 0);
io64(ioObj,888,distcode);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

TrialStart = targtime-ExpStart;

WaitSecs(pretrialtime);

PsychPortAudio('FillBuffer', pahandle, wavedata);
PsychPortAudio('Start', pahandle, 1, 0, 0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
io64(ioObj,888,1);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
WaitSecs(aimtime);  

if isoccluded
    PLATO_lens(1,0,0); % close glasses
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %lptwrite(888, 3); WaitSecs(cleartime); lptwrite(888, 0);  
    io64(ioObj,888,2);
    WaitSecs(0.005);
    io64(ioObj,888,0);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
else
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %lptwrite(888, 3); WaitSecs(cleartime); lptwrite(888, 0);  
    io64(ioObj,888,3);
    WaitSecs(0.005);
    io64(ioObj,888,0);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
WaitSecs(aimtime2);

PsychPortAudio('FillBuffer', pahandle, wavedata);
startrt = PsychPortAudio('Start', pahandle, 1, 0, 0);
startrt = GetSecs;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
io64(ioObj,888,4);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% WAIT FOR SIGNAL FROM SCATT %%%

shot = 0;
flushinput(sObj);
disp('waiting for a shot Verbal...');
while (GetSecs-startrt <=  deadline)
    [KeyIsDown, endrt, KeyCode]=KbCheck;
    if KeyIsDown           % press after stimulus
        RT = endrt-startrt;
        response = KbName(find(KeyCode)); %hopefully this will be a cell showing accuracy
        shot = 1;
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
        io64(ioObj,888,199);
        WaitSecs(0.005);
        io64(ioObj,888,0);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        if iscell(response)
            response = response{1};
        end
        if strcmpi(response,'x')
            Screen('CloseAll');
            clear all
            return
        elseif strcmpi(response,'p')
            KbStrokeWait;
        end
        break
    end
    if(sObj.BytesAvailable > 0)
        
        %Send an event code to EEG here. Maybe record a time stamp too?
        pause(0.1); %wait 100ms for the full string to be transmitted
        strBuf = fscanf(sObj);
        strPacket = strBuf(1:(length(strBuf)-1)); %remove the ':' at the end of the strBuf
        X_Y_Score = strsplit(strPacket, ',');  
        X = str2double(X_Y_Score{1});
        Y = str2double(X_Y_Score{2});
        Score = str2double(X_Y_Score{3});
        
        %convert them to meaningful numbers
        X = X/20; %conver to millimeters
        Y = Y/20; %conver to millimeters
        Score = Score/10;
        %str = sprintf('(X,Y) = (%0.2f,%0.2f) millimeters, Score = %0.1f', X, Y, Score);
        %disp(str);
        RT = GetSecs-startrt;
        shot = 1;
        response = sprintf('(X,Y) = (%0.2f,%0.2f) millimeters, Score = %0.1f', X, Y, Score);
        disp('shot made Verbal');
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
        io64(ioObj,888,5);
        WaitSecs(0.005);
        io64(ioObj,888,0);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        eqi = 0;
        myAC = response;
        for chari = 1:numel(myAC)

            if strcmp(myAC(chari),'=')
                eqi = eqi+1;
                if eqi == 2

                    scorestr = myAC(chari+2:chari+4);
                    score = round(str2double(scorestr));
                    score = 200+score;
                    disp(['score: ' num2str(score)]);
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    %lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
                    io64(ioObj,888,score);
                    WaitSecs(0.005);
                    io64(ioObj,888,0);
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    

                end
            end
        end
        
        
        break; %quit after receiving 1 shot
    end
end

if ~shot
    RT = 0;
    response = 'none';
end

fprintf(dataFile,'%s\t%s\t%s\t%i\t%i\t%s\t%f\t%s\t%f\n',subname,subjectnum,date,distcode,isoccluded,'vrep',RT,response, TrialStart);

WaitSecs(aftershottime);

mytext = 'Estimate Your Score';
Screen('DrawText',w,mytext,margin,centery);
Screen('Flip',w);

if isoccluded
    PLATO_trial(0); 
    PLATO_trial(1); %open glasses
end
KbStrokeWait();
   
mytext = 'Give Verbal Report';
Screen('DrawText',w,mytext,margin,centery);
Screen('Flip',w);
KbStrokeWait();

recObj = audiorecorder;
record(recObj, 15);
KbStrokeWait();



mkdir ('VerbRep\', subjectnum);
filepath = ['/Users/Shamsi/Documents/MATLAB/EDASI/Script/VerbRep/' subjectnum '/'];
filename = [];
%filename = [filename 'Trl' num2str(triali) '_' 'Blk' num2str(blocki) '_' subname '_' subjectnum '_' distcode '_' isoccluded];
filename = [filename 'Trl' num2str(triali) '_' 'Blk' num2str(blocki) '_' subname '_' subjectnum num2str(distcode) '_' num2str(isoccluded) ];
filename = [filepath filename '.wav'];

b = getaudiodata(recObj);
audiowrite(filename, b, 8000);


% This creates a single audio recording object
%recObj = audiorecorder;

% this allows you to record some things
%record(recObj, 15);
%KbStrokeWait();

% this puts the audio data into a file that can be saved using audio write
%b = getaudiodata(recObj);


    % this creates a single file name called: "Trial (k).wav" in 
    % C:\Users\Shamsi\Documents\MATLAB\EDASI\Script\VerbRep\
    % the file is literally called "Trial (k).wav". k is not translated
    % into a number
    
    % to translate k into a number corresponding to the value of k, 
    % you first have to translate k into a string using the function
    % num2str.  If k == 34, num2str(k) is '34'. 34 is an integer. '34' is a
    % string.  Strings can go with other strings in an array. Integers
    % cannot
    
    % say x = 30
    % if we make an array ['what is x'], it will literally output 
    % 'what is x'.
    % if we make an array ['what is ' x], it will produce an error because
    % 'what is ' (a string) and x (an integer) cannot be put into the same
    % array.  
    
    % if we make an array ['what is ' num2str(x)] it will 
    % output 'what is 30'. Notice that 'what is ' went inside of quotes and
    % num2str(x) was not inside of any quotes
    
    
    % ... but this bit of code you have written doesn't make any sense 
    % anyway because you seem to be trying to make 64 files, when the
    % variable b only contains a single audio recording. You need to create
    % a single filename here that is unique to the current trial and block. 
    % Each time VerbalRep is called, it only does a single trial. Thus it is called many
    % times in the main function at the top of this .m file. The filename you create here should
    % contain both the block (indexed by the variable blocki above in the
    % main function) and the trial (indexed by the variable triali above in
    % the main function).
    
    % I have helped you out by passing blocki and triali (both integers) into the VerbalRep
    % function, so you can use those variables in this bit of code.
    % Translate blocki and triali into strings and use them to create a
    % filename that is unique to this trial. You will do this only once,
    % NOT inside of a for loop
    

PLATO_trial(0);


function Estimate()
%Estimation Only
global w aftershottime wavedata pahandle targtex isoccluded aimtime aimtime2 pretrialtime resttime cleartime distcode deadline
global date subjectnum subname centery ioObj sObj dataFile margin TrialStart ExpStart
 
Screen('DrawTexture', w, targtex);
targtime = Screen('Flip',w); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, distcode); WaitSecs(cleartime); lptwrite(888, 0);
io64(ioObj,888,distcode);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
TrialStart = targtime-ExpStart;
WaitSecs(pretrialtime);

PsychPortAudio('FillBuffer', pahandle, wavedata);
PsychPortAudio('Start', pahandle, 1, 0, 0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, 2); WaitSecs(cleartime); lptwrite(888, 0);  
io64(ioObj,888,1);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
WaitSecs(aimtime);  

if isoccluded
    PLATO_lens(1,0,0); % close glasses
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %lptwrite(888, 3); WaitSecs(cleartime); lptwrite(888, 0); 
    io64(ioObj,888,2);
    WaitSecs(0.005);
    io64(ioObj,888,0);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    else
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %lptwrite(888, 3); WaitSecs(cleartime); lptwrite(888, 0);  
    io64(ioObj,888,3);
    WaitSecs(0.005);
    io64(ioObj,888,0);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
WaitSecs(aimtime2);

PsychPortAudio('FillBuffer', pahandle, wavedata);
startrt = PsychPortAudio('Start', pahandle, 1, 0, 0);
startrt = GetSecs;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
io64(ioObj,888,4);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% WAIT FOR SIGNAL FROM SCATT %%%

shot = 0;
flushinput(sObj);
disp('wait for shot Estimate..');
while (GetSecs-startrt <=  deadline)
    [KeyIsDown, endrt, KeyCode]=KbCheck;
    if KeyIsDown           % press after stimulus
        RT = endrt-startrt;
        response = KbName(find(KeyCode)); %hopefully this will be a cell showing accuracy
        shot = 1;
        if iscell(response)
            response = response{1};
        end
        if strcmpi(response,'x')
            Screen('CloseAll');
            clear all
            return
        elseif strcmpi(response,'p')
            KbStrokeWait;
        end
        break
    end
    if(sObj.BytesAvailable > 0)
        
        %Send an event code to EEG here. Maybe record a time stamp too?
        pause(0.1); %wait 100ms for the full string to be transmitted
        strBuf = fscanf(sObj);
        strPacket = strBuf(1:(length(strBuf)-1)); %remove the ':' at the end of the strBuf
        X_Y_Score = strsplit(strPacket, ',');  
        X = str2double(X_Y_Score{1});
        Y = str2double(X_Y_Score{2});
        Score = str2double(X_Y_Score{3});
        
        %convert them to meaningful numbers
        X = X/20; %conver to millimeters
        Y = Y/20; %conver to millimeters
        Score = Score/10;
        %str = sprintf('(X,Y) = (%0.2f,%0.2f) millimeters, Score = %0.1f', X, Y, Score);
        %disp(str);
        RT = GetSecs-startrt;
        shot = 1;
        response = sprintf('(X,Y) = (%0.2f,%0.2f) millimeters, Score = %0.1f', X, Y, Score);
        disp('shot made Estimate');
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
        io64(ioObj,888,6);
        WaitSecs(0.005);
        io64(ioObj,888,0);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        myAC = response;
        eqi = 0;
        for chari = 1:numel(myAC)

            if strcmp(myAC(chari),'=')
                eqi = eqi+1;
                if eqi == 2

                    scorestr = myAC(chari+2:chari+4);
                    score = round(str2double(scorestr));
                    score = 200+score;
                    disp(['score: ' num2str(score)]);
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    %lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
                    io64(ioObj,888,score);
                    WaitSecs(0.005);
                    io64(ioObj,888,0);
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    

                end
            end
        end
        break; %quit after receiving 1 shot
    end
end

if ~shot
    RT = 0;
    response = 'none';
end

fprintf(dataFile,'%s\t%s\t%s\t%i\t%i\t%s\t%f\t%s\t%f\n',subname,subjectnum,date,distcode,isoccluded,'estimate',RT,response, TrialStart);
% fprintf(dataFile,'%s\t%s\t%s\t%i\t%i\t%s\t%f\t%s\n',subname,subjectnum,date,distcode,isoccluded,'estimate',RT,response);

WaitSecs(aftershottime);

mytext = 'Estimate Your Score';
Screen('DrawText',w,mytext,margin,centery);
Screen('Flip',w);

if isoccluded
    PLATO_trial(0); 
    PLATO_trial(1); %open glasses
end

KbStrokeWait();
PLATO_trial(0); 

   
function Basic()

global w aftershottime wavedata pahandle targtex isoccluded aimtime aimtime2 pretrialtime resttime cleartime distcode deadline
global date subjectnum subname ioObj sObj dataFile TrialStart ExpStart

Screen('DrawTexture', w, targtex);
targtime = Screen('Flip',w); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, distcode); WaitSecs(cleartime); lptwrite(888, 0);
io64(ioObj,888,distcode);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
TrialStart = targtime-ExpStart;
WaitSecs(pretrialtime);

PsychPortAudio('FillBuffer', pahandle, wavedata);
PsychPortAudio('Start', pahandle, 1, 0, 0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, 2); WaitSecs(cleartime); lptwrite(888, 0);  
io64(ioObj,888,1);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
WaitSecs(aimtime);  

if isoccluded
    PLATO_lens(1,0,0); % close glasses
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %lptwrite(888, 3); WaitSecs(cleartime); lptwrite(888, 0);  
    io64(ioObj,888,2);
    WaitSecs(0.005);
    io64(ioObj,888,0);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
else
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %lptwrite(888, 3); WaitSecs(cleartime); lptwrite(888, 0);  
    io64(ioObj,888,3);
    WaitSecs(0.005);
    io64(ioObj,888,0);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
WaitSecs(aimtime2);

PsychPortAudio('FillBuffer', pahandle, wavedata);
startrt = PsychPortAudio('Start', pahandle, 1, 0, 0);
startrt = GetSecs;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
io64(ioObj,888,4);
WaitSecs(0.005);
io64(ioObj,888,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% WAIT FOR SIGNAL FROM SCATT %%%

shot = 0;
flushinput(sObj);
disp('wait for shot Basic...');
while (GetSecs-startrt <=  deadline)
    [KeyIsDown, endrt, KeyCode]=KbCheck;
    if KeyIsDown           % press after stimulus
        RT = endrt-startrt;
        response = KbName(find(KeyCode)); %hopefully this will be a cell showing accuracy
        shot = 1;
        if iscell(response)
            response = response{1};
        end
        if strcmpi(response,'x')
            Screen('CloseAll');
            clear all
            return
        elseif strcmpi(response,'p')
            KbStrokeWait;
        end
        break
    end
    if(sObj.BytesAvailable > 0)
        
        %Send an event code to EEG here. Maybe record a time stamp too?
        pause(0.1); %wait 100ms for the full string to be transmitted
        strBuf = fscanf(sObj);
        strPacket = strBuf(1:(length(strBuf)-1)); %remove the ':' at the end of the strBuf
        X_Y_Score = strsplit(strPacket, ',');  
        X = str2double(X_Y_Score{1});
        Y = str2double(X_Y_Score{2});
        Score = str2double(X_Y_Score{3});
        
        %convert them to meaningful numbers
        X = X/20; %conver to millimeters
        Y = Y/20; %conver to millimeters
        Score = Score/10;
        %str = sprintf('(X,Y) = (%0.2f,%0.2f) millimeters, Score = %0.1f', X, Y, Score);
        %disp(str);
        RT = GetSecs-startrt;
        shot = 1;
        response = sprintf('(X,Y) = (%0.2f,%0.2f) millimeters, Score = %0.1f', X, Y, Score);
        disp('shot made Basic');
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
        io64(ioObj,888,7);
        WaitSecs(0.005);
        io64(ioObj,888,0);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        myAC = response;
        eqi = 0;
        for chari = 1:numel(myAC)

            if strcmp(myAC(chari),'=')
                eqi = eqi+1;
                if eqi == 2

                    scorestr = myAC(chari+2:chari+4);
                    score = round(str2double(scorestr));
                    score = 200+score;
                    disp(['score: ' num2str(score)]);
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    %lptwrite(888, 4); WaitSecs(cleartime); lptwrite(888, 0);  
                    io64(ioObj,888,score);
                    WaitSecs(0.005);
                    io64(ioObj,888,0);
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    

                end
            end
        end
        break; %quit after receiving 1 shot
    end
end
disp('out of loop');
if ~shot
    RT = 0;
    response = 'none';
end

fprintf(dataFile,'%s\t%s\t%s\t%i\t%i\t%s\t%f\t%s\t%f\n',subname,subjectnum,date,distcode,isoccluded,'basic',RT,response, TrialStart);
% fprintf(dataFile,'%s\t%s\t%s\t%i\t%i\t%s\t%f\t%s\n',subname,subjectnum,date,distcode,isoccluded,'basic',RT,response);

WaitSecs(aftershottime);
if isoccluded
    PLATO_trial(0); 
    PLATO_trial(1);% open glasses see if something interesting happens after glasses are opened
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %lptwrite(888, 5); WaitSecs(cleartime); lptwrite(888, 0);  
    io64(ioObj,888,100 );
    WaitSecs(0.005);
    io64(ioObj,888,0);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
Screen('Flip',w);
WaitSecs(resttime);
PLATO_trial(0);






    
