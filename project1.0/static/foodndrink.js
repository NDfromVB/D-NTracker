document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('emonth').addEventListener('input', function(){
        if (new Set([1, 3, 5, 7, 8, 10, 12]).has(parseInt(document.getElementById('emonth').value))) {
            document.getElementById('eday').max = 31;
        } else if (parseInt(document.getElementById('emonth').value) === 2) {
            document.getElementById('eday').max = 29;
        } else {
            document.getElementById('eday').max = 30;
        }
    });

    document.getElementById('imonth').addEventListener('input', function(){
        if (new Set([1, 3, 5, 7, 8, 10, 12]).has(parseInt(document.getElementById('imonth').value))) {
            document.getElementById('iday').max = 31;
        } else if (parseInt(document.getElementById('imonth').value) === 2) {
            document.getElementById('iday').max = 29;
        } else {
            document.getElementById('iday').max = 30;
        }
    });

});

function geti0DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment();
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('iyear').value = year;
    document.getElementById('imonth').value = month;
    document.getElementById('iday').value = day;
}

function geti1DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment().clone().subtract(1,'days');
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('iyear').value = year;
    document.getElementById('imonth').value = month;
    document.getElementById('iday').value = day;
}
function geti7DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment().clone().subtract(1,'weeks');
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('iyear').value = year;
    document.getElementById('imonth').value = month;
    document.getElementById('iday').value = day;
}
function geti30DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment().clone.subtract(1, 'months');
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('iyear').value = year;
    document.getElementById('imonth').value = month;
    document.getElementById('iday').value = day;
}

function gete1DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment().clone().add(1, 'days');
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('eyear').value = year;
    document.getElementById('emonth').value = month;
    document.getElementById('eday').value = day;
}

function gete7DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment().clone().add(7, 'days');
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('eyear').value = year;
    document.getElementById('emonth').value = month;
    document.getElementById('eday').value = day;
}

function gete30DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment().clone().add(1, 'months');
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('eyear').value = year;
    document.getElementById('emonth').value = month;
    document.getElementById('eday').value = day;
}

function gete365DateInformation() {
    moment.tz.setDefault("Asia/Ho_Chi_Minh");
    const currentDate = moment().clone().add(1, 'years');
    const year = currentDate.format('YYYY');
    const month = String(parseInt(currentDate.format('MM'), 10));
    const day = String(parseInt(currentDate.format('DD'), 10));
    document.getElementById('eyear').value = year;
    document.getElementById('emonth').value = month;
    document.getElementById('eday').value = day;
}
