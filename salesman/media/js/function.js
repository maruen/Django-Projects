
function calc_counter_from_time(diff) {
   if (diff > 0) {
      hours=Math.floor(diff / 3600)
      minutes=Math.floor((diff / 3600 - hours) * 60)
      seconds=Math.round((((diff / 3600 - hours) * 60) - minutes) * 60)
   } else {
      hours = 0;
      minutes = 0;
      seconds = 0;
   }

   if (seconds == 60) {
      seconds = 0;
   }

   if (minutes < 10) {
      if (minutes < 0) {
         minutes = 0;
      }
      minutes = '0' + minutes;
                      }
      if (seconds < 10) {
         if (seconds < 0) {
            seconds = 0;
         }
         seconds = '0' + seconds;
                        }
      if (hours < 10) {
         if (hours < 0) {
            hours = 0;
         }
      hours = '0' + hours;
   }
   
   return hours + ":" + minutes + ":" + seconds;
}

