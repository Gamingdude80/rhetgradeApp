const weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}

function refreshTime(){
    var date = new Date()
    var day = weekdays[date.getDay()]
    var month = months[date.getMonth()]
    var datetime = day+" "+month+" "+date.getDate()+" - "+formatAMPM(date)
    document.getElementById("time").textContent = datetime;
}
setInterval(refreshTime, 100);