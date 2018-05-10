
# Sets time signature for 1 measure and restores the previous signature in the next measure

def run():
  # input signature for 1 measure ('34' for '3/4')
  input_res = RPR_GetUserInputs('Time Signature', 1, 'XY for X/Y', '44', 3)
  if not input_res[0]:
    return
  
  sig_str = input_res[4]
  (new_sig_up, new_sig_down) = (int(sig_str[0]), int(sig_str[1]))
  
  proj = 0
  ptidx = -1
  measurepos = -1
  beatpos = -1
  bpm = -1
  lineartempo = False
  
  cur_pos = RPR_GetCursorPosition()
  cur_time_sig_res = RPR_TimeMap_GetTimeSigAtTime(0, cur_pos, 0, 0, 0)
  (cur_timesig_num, cur_timesig_denom, cur_tempo) = (cur_time_sig_res[2], cur_time_sig_res[3], cur_time_sig_res[4])
  
  RPR_SetTempoTimeSigMarker(proj, ptidx, cur_pos, measurepos, beatpos, bpm, new_sig_up, new_sig_down, lineartempo)
  
  move_to_next_measure_id = 41040
  RPR_Main_OnCommand(move_to_next_measure_id, 0)

  cur_pos = RPR_GetCursorPosition()
  RPR_SetTempoTimeSigMarker(proj, ptidx, cur_pos, measurepos, beatpos, bpm, cur_timesig_num, cur_timesig_denom, lineartempo)
  
  RPR_UpdateTimeline()


def tests():
  pass
  
  # RPR_ShowMessageBox(str(RPR_GetCursorPosition()), '', 0)
  RPR_ShowConsoleMsg(str(RPR_GetCursorPosition()))
  
  # --- examples ---
  
  # -- API :: (proj - 0 for current; ptidx - -1 to add; timepos - float time in seconds; measurepos, beatpos - 0-based, for 8.2 -> 7,1; bpm - tempo; timesig_num - signature numerator;  timesig_denom - signature denominator; lineartempo - boolean for the checkbox)
  # RPR_SetTempoTimeSigMarker(proj, ptidx, timepos, measurepos, beatpos, bpm, timesig_num, timesig_denom, lineartempo)
  
  # -- at current position (play time as float in seconds) set 3/4 time signature; set tempo to 152
  # cur_pos = RPR_GetCursorPosition()
  # RPR_SetTempoTimeSigMarker(0, -1, cur_pos, -1, -1, -1, 3, 4, False)
  # RPR_SetTempoTimeSigMarker(0, -1, cur_pos, -1, -1, 152, 0, 0, False)
  
  # -- set sig to 3/4 at bar 9; to 4/4 at bar 10 (0-based)
  # RPR_SetTempoTimeSigMarker(0, -1, -1, 8, 0, -1, 3, 4, False)
  # RPR_SetTempoTimeSigMarker(0, -1, -1, 9, 0, -1, 4, 4, False)
  
# ---

run()
# tests()
