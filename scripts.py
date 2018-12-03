feats = ["LEVEL_T1", "LEVEL_T2", "LEVEL_T3", "LEVEL_T4", "LEVEL_T5", "LEVEL_T6",
         "LEVEL_T7", "PRESSURE_J280", "PRESSURE_J269", "PRESSURE_J300", "PRESSURE_J256",
         "PRESSURE_J289", "PRESSURE_J415", "PRESSURE_J302", "PRESSURE_J306", "PRESSURE_J307",
         "PRESSURE_J317", "PRESSURE_J14", "PRESSURE_J422", "FLOW_PU1", "FLOW_PU2", "FLOW_PU3",
         "FLOW_PU4", "FLOW_PU5", "FLOW_PU6", "FLOW_PU7", "FLOW_PU8", "FLOW_PU9", "FLOW_PU10",
         "FLOW_PU11", "FLOW_V2"]

for feat in feats:
        delta_col = "{}_DELTA".format(feat)
        abs_delta_col = "{}_ABS_DELTA".format(feat)

        print("test <- test %>% mutate({} = abs({} - lag({})))".format(delta_col, feat, feat))
