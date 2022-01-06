
def run():
  left_edge = -0.01
  
  # (Boolean isSet, Boolean isLoop, Float startOut, Float endOut, Boolean allowautoseek) = RPR_GetSet_LoopTimeRange(isSet, isLoop, startOut, endOut, allowautoseek)
  # startOut, endOut (seconds)
  
  res = RPR_GetSet_LoopTimeRange(0,0,0,0,0)
  st, en = res[2], res[3]
  RPR_GetSet_LoopTimeRange(True, False, st + left_edge, en, False)
  

# ---
run()
