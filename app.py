[     UTC     ] Logs for dashboardmelina-kish-2a57tywg3eghhffwjapp3hc.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:17:34.866 503 GET /script-health-check (127.0.0.1) 1528.98ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:17:39.679 503 GET /script-health-check (127.0.0.1) 1373.77ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:17:44.811 503 GET /script-health-check (127.0.0.1) 1483.56ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:17:49.762 503 GET /script-health-check (127.0.0.1) 1509.70ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:17:54.724 503 GET /script-health-check (127.0.0.1) 1474.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:17:59.749 503 GET /script-health-check (127.0.0.1) 1506.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:04.758 503 GET /script-health-check (127.0.0.1) 1423.47ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:09.826 503 GET /script-health-check (127.0.0.1) 1578.83ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:14.568 503 GET /script-health-check (127.0.0.1) 1332.08ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:20.041 503 GET /script-health-check (127.0.0.1) 1737.76ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:24.750 503 GET /script-health-check (127.0.0.1) 1509.92ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:29.850 503 GET /script-health-check (127.0.0.1) 1613.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:34.730 503 GET /script-health-check (127.0.0.1) 1475.86ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:39.723 503 GET /script-health-check (127.0.0.1) 1480.29ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:44.814 503 GET /script-health-check (127.0.0.1) 1582.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:49.614 503 GET /script-health-check (127.0.0.1) 1378.32ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:54.756 503 GET /script-health-check (127.0.0.1) 1446.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:18:59.885 503 GET /script-health-check (127.0.0.1) 1612.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:04.923 503 GET /script-health-check (127.0.0.1) 1643.99ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:09.944 503 GET /script-health-check (127.0.0.1) 1661.65ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:14.971 503 GET /script-health-check (127.0.0.1) 1651.10ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:19.764 503 GET /script-health-check (127.0.0.1) 1510.95ms

[13:19:23] 🐙 Pulling code changes from Github...

2025-06-11 13:19:24.312 Received event for non-watched file: /mount/src/dashboard_melina-kish/app.py

2025-06-11 13:19:24.312 Received event for non-watched file: /mount/src/dashboard_melina-kish/app.py

[13:19:24] 📦 Processing dependencies...

[13:19:24] 📦 Processed dependencies!

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    65 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    66 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

  ❱ 67 timeline_df["AC"] = filtered_df["Actual Cost"].fillna(0).cumsum()        

    68                                                                          

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:24.803 503 GET /script-health-check (127.0.0.1) 1500.20ms

[13:19:26] 🔄 Updated app!

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:32.452 503 GET /script-health-check (127.0.0.1) 4211.13ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:35.906 503 GET /script-health-check (127.0.0.1) 2583.40ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:39.665 503 GET /script-health-check (127.0.0.1) 1383.33ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:46.485 503 GET /script-health-check (127.0.0.1) 3072.63ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:49.961 503 GET /script-health-check (127.0.0.1) 1721.19ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:55.930 503 GET /script-health-check (127.0.0.1) 2674.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:19:59.911 503 GET /script-health-check (127.0.0.1) 1631.48ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:05.060 503 GET /script-health-check (127.0.0.1) 1715.36ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:09.891 503 GET /script-health-check (127.0.0.1) 1639.89ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:15.075 503 GET /script-health-check (127.0.0.1) 1743.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:19.897 503 GET /script-health-check (127.0.0.1) 1621.61ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:25.187 503 GET /script-health-check (127.0.0.1) 1888.19ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:29.873 503 GET /script-health-check (127.0.0.1) 1577.50ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:35.241 503 GET /script-health-check (127.0.0.1) 1922.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:39.979 503 GET /script-health-check (127.0.0.1) 1651.85ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:44.783 503 GET /script-health-check (127.0.0.1) 1488.48ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:49.838 503 GET /script-health-check (127.0.0.1) 1564.32ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:54.912 503 GET /script-health-check (127.0.0.1) 1583.91ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:20:59.788 503 GET /script-health-check (127.0.0.1) 1518.63ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:04.730 503 GET /script-health-check (127.0.0.1) 1493.54ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:09.934 503 GET /script-health-check (127.0.0.1) 1699.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:14.763 503 GET /script-health-check (127.0.0.1) 1548.72ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:19.766 503 GET /script-health-check (127.0.0.1) 1434.45ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:24.922 503 GET /script-health-check (127.0.0.1) 1687.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:29.867 503 GET /script-health-check (127.0.0.1) 1514.69ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:34.723 503 GET /script-health-check (127.0.0.1) 1427.91ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:39.768 503 GET /script-health-check (127.0.0.1) 1536.08ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:44.614 503 GET /script-health-check (127.0.0.1) 1395.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:49.800 503 GET /script-health-check (127.0.0.1) 1565.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:54.812 503 GET /script-health-check (127.0.0.1) 1594.61ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:21:59.881 503 GET /script-health-check (127.0.0.1) 1644.75ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:04.724 503 GET /script-health-check (127.0.0.1) 1479.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:09.896 503 GET /script-health-check (127.0.0.1) 1660.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:14.833 503 GET /script-health-check (127.0.0.1) 1613.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:19.772 503 GET /script-health-check (127.0.0.1) 1555.28ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:24.638 503 GET /script-health-check (127.0.0.1) 1407.50ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:29.647 503 GET /script-health-check (127.0.0.1) 1424.04ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:34.781 503 GET /script-health-check (127.0.0.1) 1539.32ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:39.939 503 GET /script-health-check (127.0.0.1) 1643.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:44.651 503 GET /script-health-check (127.0.0.1) 1430.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:49.668 503 GET /script-health-check (127.0.0.1) 1346.30ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:54.584 503 GET /script-health-check (127.0.0.1) 1350.96ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:22:59.743 503 GET /script-health-check (127.0.0.1) 1480.86ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:04.594 503 GET /script-health-check (127.0.0.1) 1373.75ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:09.877 503 GET /script-health-check (127.0.0.1) 1608.04ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:14.690 503 GET /script-health-check (127.0.0.1) 1453.47ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:19.800 503 GET /script-health-check (127.0.0.1) 1511.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:24.609 503 GET /script-health-check (127.0.0.1) 1290.48ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:29.714 503 GET /script-health-check (127.0.0.1) 1484.61ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:34.766 503 GET /script-health-check (127.0.0.1) 1453.52ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:39.665 503 GET /script-health-check (127.0.0.1) 1343.31ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:44.795 503 GET /script-health-check (127.0.0.1) 1505.66ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:50.481 503 GET /script-health-check (127.0.0.1) 2201.17ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:54.725 503 GET /script-health-check (127.0.0.1) 1499.92ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:23:59.776 503 GET /script-health-check (127.0.0.1) 1539.31ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:04.846 503 GET /script-health-check (127.0.0.1) 1593.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:09.868 503 GET /script-health-check (127.0.0.1) 1635.73ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:14.850 503 GET /script-health-check (127.0.0.1) 1532.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:19.668 503 GET /script-health-check (127.0.0.1) 1416.98ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:24.645 503 GET /script-health-check (127.0.0.1) 1369.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:29.729 503 GET /script-health-check (127.0.0.1) 1479.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:34.796 503 GET /script-health-check (127.0.0.1) 1559.85ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:39.913 503 GET /script-health-check (127.0.0.1) 1635.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:44.845 503 GET /script-health-check (127.0.0.1) 1590.37ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:49.810 503 GET /script-health-check (127.0.0.1) 1513.77ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:54.881 503 GET /script-health-check (127.0.0.1) 1573.04ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:24:59.898 503 GET /script-health-check (127.0.0.1) 1608.73ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:04.928 503 GET /script-health-check (127.0.0.1) 1591.74ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:10.006 503 GET /script-health-check (127.0.0.1) 1726.70ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:14.865 503 GET /script-health-check (127.0.0.1) 1533.73ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:19.852 503 GET /script-health-check (127.0.0.1) 1526.43ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:24.795 503 GET /script-health-check (127.0.0.1) 1541.17ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:30.717 503 GET /script-health-check (127.0.0.1) 2148.67ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:35.614 503 GET /script-health-check (127.0.0.1) 2243.67ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:40.397 503 GET /script-health-check (127.0.0.1) 1972.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:45.424 503 GET /script-health-check (127.0.0.1) 2023.10ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:50.662 503 GET /script-health-check (127.0.0.1) 2250.76ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:25:55.466 503 GET /script-health-check (127.0.0.1) 2004.98ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:00.443 503 GET /script-health-check (127.0.0.1) 2023.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:05.562 503 GET /script-health-check (127.0.0.1) 2130.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:10.291 503 GET /script-health-check (127.0.0.1) 1945.22ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:15.420 503 GET /script-health-check (127.0.0.1) 2016.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:20.541 503 GET /script-health-check (127.0.0.1) 1904.39ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:25.540 503 GET /script-health-check (127.0.0.1) 2211.76ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:30.610 503 GET /script-health-check (127.0.0.1) 2169.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:35.570 503 GET /script-health-check (127.0.0.1) 2176.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:40.453 503 GET /script-health-check (127.0.0.1) 1910.40ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:45.288 503 GET /script-health-check (127.0.0.1) 1943.38ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:50.507 503 GET /script-health-check (127.0.0.1) 1885.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:26:55.458 503 GET /script-health-check (127.0.0.1) 2096.32ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:00.215 503 GET /script-health-check (127.0.0.1) 1843.98ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:05.286 503 GET /script-health-check (127.0.0.1) 1901.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:10.032 503 GET /script-health-check (127.0.0.1) 1702.02ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:15.027 503 GET /script-health-check (127.0.0.1) 1696.50ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:19.876 503 GET /script-health-check (127.0.0.1) 1604.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:24.844 503 GET /script-health-check (127.0.0.1) 1522.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:29.705 503 GET /script-health-check (127.0.0.1) 1382.46ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:34.800 503 GET /script-health-check (127.0.0.1) 1479.64ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:39.871 503 GET /script-health-check (127.0.0.1) 1555.13ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:44.764 503 GET /script-health-check (127.0.0.1) 1533.78ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:49.720 503 GET /script-health-check (127.0.0.1) 1486.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:54.794 503 GET /script-health-check (127.0.0.1) 1468.48ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:27:59.810 503 GET /script-health-check (127.0.0.1) 1535.45ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:04.765 503 GET /script-health-check (127.0.0.1) 1508.99ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:09.979 503 GET /script-health-check (127.0.0.1) 1677.50ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:14.817 503 GET /script-health-check (127.0.0.1) 1565.45ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:19.895 503 GET /script-health-check (127.0.0.1) 1558.74ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:24.658 503 GET /script-health-check (127.0.0.1) 1419.48ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:29.908 503 GET /script-health-check (127.0.0.1) 1661.60ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:34.826 503 GET /script-health-check (127.0.0.1) 1585.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:39.692 503 GET /script-health-check (127.0.0.1) 1459.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:44.768 503 GET /script-health-check (127.0.0.1) 1526.78ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:49.881 503 GET /script-health-check (127.0.0.1) 1567.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:54.749 503 GET /script-health-check (127.0.0.1) 1436.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:28:59.792 503 GET /script-health-check (127.0.0.1) 1541.17ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:04.888 503 GET /script-health-check (127.0.0.1) 1634.39ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:09.892 503 GET /script-health-check (127.0.0.1) 1566.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:14.760 503 GET /script-health-check (127.0.0.1) 1471.85ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:19.678 503 GET /script-health-check (127.0.0.1) 1416.05ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:24.905 503 GET /script-health-check (127.0.0.1) 1592.59ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:29.857 503 GET /script-health-check (127.0.0.1) 1530.13ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:34.776 503 GET /script-health-check (127.0.0.1) 1525.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:39.643 503 GET /script-health-check (127.0.0.1) 1403.34ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:44.900 503 GET /script-health-check (127.0.0.1) 1548.34ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:49.843 503 GET /script-health-check (127.0.0.1) 1565.93ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:29:54.832 503 GET /script-health-check (127.0.0.1) 1557.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:00.527 503 GET /script-health-check (127.0.0.1) 2162.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:05.100 503 GET /script-health-check (127.0.0.1) 1768.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:10.160 503 GET /script-health-check (127.0.0.1) 1821.52ms

[13:30:13] 🐙 Pulling code changes from Github...

[13:30:14] 📦 Processing dependencies...

[13:30:14] 📦 Processed dependencies!

2025-06-11 13:30:14.582 Received event for non-watched file: /mount/src/dashboard_melina-kish/app.py

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 fig_trend_bar.update_layout(title="میله‌ای تجمعی پیشرفت")                 

    65 st.plotly_chart(fig_trend_bar, use_container_width=True)                 

    66                                                                          

  ❱ 67 # 📉 نمودار S Curve (PV / EV / AC)                                       

    68 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    69 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

    70 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:15.229 503 GET /script-health-check (127.0.0.1) 1882.80ms

[13:30:16] 🔄 Updated app!

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:19.951 503 GET /script-health-check (127.0.0.1) 1645.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:25.044 503 GET /script-health-check (127.0.0.1) 1687.75ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:30.287 503 GET /script-health-check (127.0.0.1) 1918.64ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:36.184 503 GET /script-health-check (127.0.0.1) 2913.42ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:41.463 503 GET /script-health-check (127.0.0.1) 3110.67ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:45.298 503 GET /script-health-check (127.0.0.1) 1957.12ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:50.095 503 GET /script-health-check (127.0.0.1) 1729.62ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:30:55.089 503 GET /script-health-check (127.0.0.1) 1740.90ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:31:00.113 503 GET /script-health-check (127.0.0.1) 1802.78ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:31:05.299 503 GET /script-health-check (127.0.0.1) 1932.23ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:31:10.137 503 GET /script-health-check (127.0.0.1) 1794.63ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:31:14.860 503 GET /script-health-check (127.0.0.1) 1579.17ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3812 in get_loc                                                             

                                                                                

    3809 │   │   """                                                            

    3810 │   │   casted_key = self._maybe_cast_indexer(key)                     

    3811 │   │   try:                                                           

  ❱ 3812 │   │   │   return self._engine.get_loc(casted_key)                    

    3813 │   │   except KeyError as err:                                        

    3814 │   │   │   if isinstance(casted_key, slice) or (                      

    3815 │   │   │   │   isinstance(casted_key, abc.Iterable)                   

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:167                                 

                                                                                

  in pandas._libs.index.IndexEngine.get_loc:196                                 

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7088                     

                                                                                

  in pandas._libs.hashtable.PyObjectHashTable.get_item:7096                     

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'


The above exception was the direct cause of the following exception:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/dashboard_melina-kish/app.py:67 in <module>                        

                                                                                

    64 # 📉 نمودار S Curve (PV / EV / AC)                                       

    65 st.subheader("📉 نمودار S Curve (EV / PV / AC)")                         

    66 timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()           

  ❱ 67 timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()            

    68 timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()                 

    69 fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"]  

    70 │   │   │   │   │     labels={"value": "ارزش تجمعی", "Start_Date": "تار  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4107   

  in __getitem__                                                                

                                                                                

     4104 │   │   if is_single_key:                                             

     4105 │   │   │   if self.columns.nlevels > 1:                              

     4106 │   │   │   │   return self._getitem_multilevel(key)                  

  ❱  4107 │   │   │   indexer = self.columns.get_loc(key)                       

     4108 │   │   │   if is_integer(indexer):                                   

     4109 │   │   │   │   indexer = [indexer]                                   

     4110 │   │   else:                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  

  y:3819 in get_loc                                                             

                                                                                

    3816 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      

    3817 │   │   │   ):                                                         

    3818 │   │   │   │   raise InvalidIndexError(key)                           

  ❱ 3819 │   │   │   raise KeyError(key) from err                               

    3820 │   │   except TypeError:                                              

    3821 │   │   │   # If we have a listlike key, _check_indexing_error will r  

    3822 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  

────────────────────────────────────────────────────────────────────────────────

KeyError: 'Actual Cost'

2025-06-11 13:31:19.899 503 GET /script-health-check (127.0.0.1) 1633.12ms
