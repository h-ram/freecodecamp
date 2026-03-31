function wakeUpAlarm(alarm, wake) {
  const [ah, am] = alarm.split(":").map(Number);
  const [wh, wm] = wake.split(":").map(Number);

  const alarmMinutes = ah * 60 + am;
  const wakeMinutes = wh * 60 + wm;

  const diff = wakeMinutes - alarmMinutes;

  if (diff < 0) return "early";
  if (diff <= 10) return "on time";
  return "late";
}
