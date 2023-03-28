const startTime=10;
let time=startTime*60*60;
const countDown=document.getElementById('Time_Countdown');
setInterval(update,1000);
function update(){
const hour=Math.floor(time/3600);
let minutes=Math.floor((time%3600)/60);
let second=time%60;
second=second<10 ? '0'+second:second;
minutes=minutes<10 ? '0'+minutes:minutes;
countDown.innerHTML=` ${hour} : ${minutes}: ${second}`;
time--;
}