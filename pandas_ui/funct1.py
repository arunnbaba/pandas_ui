#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#######################################################################################################
from __future__ import print_function
get_ipython().run_line_magic('matplotlib', 'inline')
import functools
import ipywidgets as widgets
import pandas as pd
from IPython.display import clear_output
from ipywidgets import Layout, Button, Box, VBox
import pandas as pd
import qgrid
from IPython.display import display
import functools
from IPython.display import clear_output
from ipywidgets import Layout, Button, Box, VBox
from traitlets import Unicode, Bool, validate, TraitError
from ipywidgets import DOMWidget, register
import pandas_profiling as pp
from ipywidgets import HBox, Label, Layout
from bokeh.io import output_file, reset_output, output_notebook
from bokeh.plotting import figure, show
import numbers
import decimal
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sys
from IPython.display import display, HTML;import os

    

#Main Class:
class student:

    #######################################################################################################
    #Static variable
    exp = [0,0]
    expr = [0,0]
    dataf = 0
    dataff = 0
    qidget = 0
    dflength = 0
    summ = 0
    wid = 0
    wid_value = 0
    r_name = 0
    flt_cnt = 1
    upd_cnt = 1
    srt_cnt = 1
    code_list = list()
    stu_out = 0
    split_df = 0
    dest_cnt = 0
    const_cnt = 0
    grp_cnt = 1
    flto = 0
    pivotdf = 0
    meltdf = 0
    org_df = 0
    temp = 0
    org = 0
    #######################################################################################################
    #Constructor
    def __init__(self):

        try:
            expa = student.dataf.columns
        except:
            expa = [0, 0]
        self.ea = widgets.Dropdown(
            options=expa, value=None, description='Column(s): ')

        expb = ['==','!=', '>', '<', '<=', '>=']
        self.eb = widgets.Dropdown(
            options=expb, value=None, description='Condition: ')

        self.tx = widgets.Text(description='Selected: ', placeholder='bin')

        expo = ['&', '|']
        self.eo = widgets.Dropdown(
            options=expo, value=None, description='relation: ')

        try:
            cs_val = student.dataf.columns
        except:
            cs_val = [0, 0]
        self.cs_dropdown = widgets.Dropdown(
            options=cs_val, value=cs_val[0], description='Column: ')

        css_val = ['Ascending(A-Z)', 'Descending(Z-A)']
        self.css_dropdown = widgets.Dropdown(
            options=css_val, value=css_val[0], description='Order : ')


        try:
            axpa = student.dataf.columns
        except:
            axpa = [0, 0]
        self.aa =  widgets.Dropdown(options=axpa,value=axpa[0], description='Column: ' )

        axpb = ['has value','contains','startswith','endswith','==','!=','>','<', '<=', '>=']
        self.ab= widgets.Dropdown(options=axpb,value=None, description='Condition: ' )

        self.ax =  widgets.Text(description = 'Selected: ', placeholder ='bin')

        axpo = ['&','|']
        self.ao= widgets.Dropdown(options=axpo,value=None, description='relation: ' )
        const_cnt =  student.const_cnt
        const_cnt += 1
        student.const_cnt = const_cnt


        ops_val = ['count','sum','mean','median','min','max','first','last','std','var']
        self.ops = widgets.Dropdown(options=ops_val,value=ops_val[0],description='Calculate :' )

        try:
            col_val = student.dataf.columns
        except:
            col_val = [0, 0]
        self.col =  widgets.Dropdown(options=col_val,value=col_val[0], description='of:       ' )


        def __del__(self): 
            dest_cnt =  student.dest_cnt
            dest_cnt += 1
            student.dest_cnt =  dest_cnt
            display('destructor called')


    #######################################################################################################
    def textbox_func(self,
                     value='textbox',
                     placeholder='textbox',
                     description='Textbox'):

        t_box = widgets.Text(
            value=value,
            placeholder=placeholder,
            description=description,
            disabled=False)

        return t_box

    #######################################################################################################
    #Function to get qgrid and df_length

    @classmethod
    def get_qwidget(cls):

        df = cls.dataf

        qwidget = qgrid.show_grid(
            df,
            show_toolbar=True,
            grid_options=({
                'fullWidthRows': True,
                'syncColumnCellResize': True,
                'defaultColumnWidth': 100,
                'forceFitColumns': False,
                'rowHeight': 28,
                'enableColumnReorder': True,
                'enableTextSelectionOnCells': True,
                'editable': True,
                'maxVisibleRows': 6,
                'autoEdit': False
            }),
            column_options=({
                'editable': True
            }))

        #Deteriming the lenght of the dataframe
        dflength = widgets.Label(value=str(df.shape[0]) + ' rows * ' +
                                 str(df.shape[1]) + ' Columns')

        cls.qwidget = qwidget
        cls.dflength = dflength
        #Returning values:
        return cls.qwidget, cls.dflength

    #######################################################################################################
    #Function to get qgrid and df_length

    @classmethod
    def get_temp_qwidget(cls, dff):

        df = dff

        qwidget_temp = qgrid.show_grid(
            df,
            show_toolbar=True,
            grid_options=({
                'fullWidthRows': False,
                'syncColumnCellResize': False,
                'defaultColumnWidth': 300,
                'forceFitColumns': False,
                'rowHeight': 28,
                'enableColumnReorder': True,
                'enableTextSelectionOnCells': True,
                'editable': True,
                'maxVisibleRows': 6,
                'autoEdit': False
            }),
            column_options=({
                'editable': True
            }))

        display(qwidget_temp)

    #######################################################################################################
    #Function to get initial widgets

    @classmethod
    def cls_dropdown_func(cls):

        df = cls.dataf

        k = [i for i in df.columns]

        wid = widgets.Dropdown(
            options=k,
            value=k[0],
            description='Column :',
            disabled=False,
            layout=Layout(width='500px', height='30px'))
        cls.wid = wid
        return cls.wid

    #######################################################################################################
    #Function to display the column level outputs

    @classmethod
    def disp_summ(cls):

        dff = cls.dataf
        wid_value = cls.wid_value

        if dff.dtypes[wid_value] not in [object]:
            a = dff[str(wid_value)].describe()

            summ = pd.DataFrame()

            for key, value in zip(a.keys(), a.values):
                summ['Keys'] = a.keys()
                summ['Value'] = a.values

            summ.header = False
            summ = summ.style.bar(subset=['Value'], color='skyblue')

            df_out = widgets.Output()

            with df_out:
                display(summ)

        else:

            summ = dff[str(wid_value)].describe(include='object')
            summ = summ.to_frame()

            df_out = widgets.Output()

            with df_out:
                display(summ)

        cls.summ = df_out

        return cls.summ

    #######################################################################################################
    #function to display column level diagrams

    @classmethod
    def dig(cls):

        df = cls.dataf

        wid_value = cls.wid_value

        fig = go.Histogram(x=df[wid_value])

        tb = widgets.Text(description='No of bins: ', placeholder='bin')
        histo = go.FigureWidget(data=[fig])

        def response(change):

            with histo.batch_update():
                if tb.value == '':
                    histo.data[0].nbinsx = 0
                else:
                    histo.data[0].nbinsx = int(tb.value)

        tb.observe(response, names="value")
        label_layout11 = Layout(width='50px', height='50px')
        tbb = HBox([Label('', layout=label_layout11), tb])
        hbb = VBox([tbb, histo])
        display(hbb)


#######################################################################################################
#######################################################################################################


def pandas_ui1(path):
    
    #######################################################################################################\
    #######################################################################################################
    
    #Accordion layout
    label_layout = Layout(width='0px', height='50px')
    label_layout1 = Layout(width='10px', height='50px')
    label_layout11 = Layout(width='50px', height='50px')
    label_layout2 = Layout(width='60px', height='50px')
    label_layout3 = Layout(width='100px', height='30px')
    label_layout4 = Layout(width='100px', height='30px')
    label_layout5 = Layout(width='150px', height='30px')
    bb_layout = Layout(width='60px', height='35px', border='2px solid orange')
    bhbf_layout = Layout(width='250px', height='35px', border='2px solid white')
    bh_layout = Layout(width='200px', height='35px', border='2px solid white')
    bt_layout = Layout(width='100px', height='35px', border='2px solid lightblue')
    bc_layout = Layout(width='35px', height='35px', border='2px solid red')

    #######################################################################################################
    #######################################################################################################

    #Accordion default widget

    lineout = widgets.Output(layout={'border': '1px solid black'})
    hd_lineout1 = widgets.Output(layout={'border': '2px solid green'})

    #######################################################################################################
    #######################################################################################################

    #widget Initialization:

    #df = pd.read_csv(r'C:\Users\thaarunn\Desktop\titanic.csv')
    df  = pd.read_csv(path)
    stu = student()
    ########
    student.exp = [0,0]
    student.expr = [0,0]
    student.dataf = 0
    student.dataff = 0
    student.qidget = 0
    student.dflength = 0
    student.summ = 0
    student.wid = 0
    student.wid_value = 0
    student.r_name = 0
    student.flt_cnt = 1
    student.upd_cnt = 1
    student.srt_cnt = 1
    student.code_list = list()
    student.stu_out = 0
    student.split_df = 0
    student.dest_cnt = 0
    student.const_cnt = 0
    student.grp_cnt = 1
    student.flto = 0
    student.pivotdf = 0
    student.meltdf = 0
    
    student.org_df = 0
    student.temp = 0
    student.org = 0
    ##@ Changing class variable
    student.dataf = df
    
    student.org_df = df
    wid_val = stu.wid_value
    wid = stu.cls_dropdown_func()

    #######################################################################################################
    #######################################################################################################

    #Accordion output
    aout = widgets.Output()

    #######################################################################################################
    #######################################################################################################


    #Python code function:
    def py_exec(x):

        if x == 'rename':
            df = student.dataf
            a = student.wid_value
            b = student.r_name
            #sq = '\\' + '\''
            sq = '\''
            c = 'df.rename(columns={' + sq + a + sq + ':' + sq + b + sq + '})'
            try:
                df = eval(c)
            except:
                js = '<script>alert("Exception raised with the option selected, Please go BACK ");</script>';display(HTML(js));raise
            student.dataf = df

            student.code_list.append(c)


    #######################################################################################################
    #General functions:
    def head_buttons_disp1(x):
        head_label = widgets.HTML(value="<b>" + x + "</b>", layout=bh_layout)
        
        head = HBox([
                bctb,
                Label('', layout=label_layout3),
                Label('', layout=bhbf_layout), head_label,
                Label('', layout=label_layout5),
                Label('', layout=label_layout3), btc
            ])
        display(hd_lineout1)
        display(head)
        display(hd_lineout1)

        
    def head_buttons_disp(x, co=False, cf=False, tb=False):
        

        #head_label = Label(x, layout=bh_layout)
        head_label = widgets.HTML(value="<b>" + x + "</b>", layout=bh_layout)

        head = HBox([
            bb,
            Label('', layout=label_layout3),
            Label('', layout=bhbf_layout), head_label,
            Label('', layout=label_layout4), bt,
            Label('', layout=label_layout3), bc
        ])

        if tb == True:

            #             head = HBox([bctb,Label('',layout=label_layout3),Label('',layout=bhbf_layout),head_label,Label('',layout=label_layout4),btt,Label('',layout=label_layout3),btc])

            head = HBox([
                bctb,
                Label('', layout=label_layout3),
                Label('', layout=bhbf_layout), head_label,
                Label('', layout=label_layout5),
                Label('', layout=label_layout3), btc
            ])

        if co == True:

            head = HBox([
                bcb,
                Label('', layout=label_layout3),
                Label('', layout=bhbf_layout), head_label,
                Label('', layout=label_layout5),
                Label('', layout=label_layout3), bc
            ])

        if cf == True:
            head = HBox([
                Label('', layout=label_layout5),
                Label('', layout=label_layout3),
                Label('', layout=bhbf_layout), head_label,
                Label('', layout=label_layout5),
                Label('', layout=label_layout3), bc
            ])

        display(hd_lineout1)
        display(head)
        display(hd_lineout1)


    #######################################################################################################
    

        #@changing static variable
    #     student.flt_cnt = 1
    #     cnt = 0
    #     for i in range(len(flt_val['ea'])):
    #         cnt += 1
    #         key = 'stu'+ str(cnt)
    #         st =  "del "+key
    #         exec(st)

        
        #if tb == True:
        #    tab_out_disp(accordion)
        #else:
        #primary_disp()


    #######################################################################################################


    def filter_func(co_wid, tb=False):

        clear_output()
        x = co_wid
        clear_output()

        tb_val = tb
        #head_buttons_disp(x, tb=True, co = True)
        if tb_val == True:
            head_buttons_disp1(x)
        else:
            head_buttons_disp(x, tb=False, co = True)
#         if tb_val == True:
#             print('inside ture')
#             head_buttons_disp(x, tb='True', co = True)
#         else:
#             print('inside false')
#             head_buttons_disp(x, tb=False, co = True)

        
        flt_dict = dict()

        #stu1 = student()

        flt_dict['stu1'] = student()
        student.flt_cnt += 1

        key_val = flt_dict['stu1']

        el_layout = Layout(width='2px', height='0px')
        el = widgets.Label("", Layout=el_layout)

        ea = key_val.ea
        eb = key_val.eb
        tx = key_val.tx
        eo = key_val.eo
        
        Hb1 = HBox([ea, eb, tx])
        vb = VBox([el, Hb1, el])
        #display(vb)

        ba = widgets.Button(description='Add Condition')
        ba.style.button_color = 'lightgray'

        bs = widgets.Button(description='Execute')
        bs.style.button_color = 'green'

        Hbb = HBox([ba, bs])
        
        def select_cd(dicto, expr_dict, seldropz):

            flt_val = dicto
            df = student.dataf
            #display(seldropz)
            sq = '\''

            int_dtypes = ['int', 'int8', 'int16', 'int32', 'int64']

            flt_dtypes = ['float', 'float16', 'float32', 'float64']

            eval_st = 'df['
            for i in range(len(flt_val['ea'])):
                #display('inside loop')

                if df[flt_val['ea'][i]].dtype in int_dtypes:
                    flt_val['tx'][i] = int(flt_val['tx'][i])

                elif df[flt_val['ea'][i]].dtype in flt_dtypes:
                    flt_val['tx'][i] = float(flt_val['tx'][i])

                value_type = type(flt_val['tx'][i])
                #display(seldropz)
                if seldropz == 'Drop rows':
                    #print('insed drop rtows')
                    flt_val['eb'][i] = expr_dict[flt_val['eb'][i]]
                    #print(flt_val['eb'][i])

                if flt_val['eo'][i] != None:
                    eval_st += flt_val['eo'][i]

                eval_st += '(df[' + sq + '{fval}'.format(fval=flt_val['ea'][i])
                eval_st += sq + '] ' + '{sval}'.format(sval=flt_val['eb'][i])

                if value_type == int or value_type == float:
                    eval_st += '{tval})'.format(tval=flt_val['tx'][i])
                else:
                    eval_st += sq + '{tval}'.format(tval=flt_val['tx'][i])
                    eval_st += sq + ' )'

            eval_st += ']'
            #display(eval_st)
            try:
                df = eval(eval_st)
            except:
                js = '<script>alert("Exception raised with the option selected, Please go BACK ");</script>';display(HTML(js));raise

            student.code_list.append(eval_st)
            student.dataf = df
            primary_disp()

        def on_ba_clicked(cntrl):
            cnt = student.flt_cnt
            cnt = str(cnt)

            #el_layout = Layout(width='2px',height='2px')
            el = widgets.Label("")

            nxt_key = 'stu' + cnt

            flt_dict[nxt_key] = student()
            student.flt_cnt += 1

            nxt_key = flt_dict[nxt_key]

            ea = nxt_key.ea
            eb = nxt_key.eb
            tx = nxt_key.tx
            eo = nxt_key.eo

            Hb2 = HBox([ea, eb, tx])
            vb.children += (eo, el, Hb2, el)

        def on_bsf_clicked(cntrl, seldr):
            #display('#',seldrop.value)
            #display('#',tb_val)
            flt_val = dict()
            ea_val = list()
            eb_val = list()
            tx_val = list()
            eo_val = list()

            for d_keys in flt_dict.keys():

                d_keys = flt_dict[d_keys]

                ea_val.append(d_keys.ea.value)
                eb_val.append(d_keys.eb.value)
                tx_val.append(d_keys.tx.value)
                eo_val.append(d_keys.eo.value)

                del d_keys
            #display(ea_val, eb_val, tx_val)

            flt_val['ea'] = ea_val
            flt_val['eb'] = eb_val
            flt_val['tx'] = tx_val
            flt_val['eo'] = eo_val

            altr = ['!=', '==', '<=', '>=', '>', '<']

            expr = ['==', '!=', '>', '<', '<=', '>=']

            expr_dict = dict()

            for i, j in zip(expr, altr):
                expr_dict[i] = j

            select_cd(flt_val, expr_dict, seldropz =  seldrop.value)
        
        sdopt = ['Select rows', 'Drop rows']
        seldrp = widgets.Dropdown(
            options=sdopt, value=sdopt[0], description='Select/Drop: ')

        sdopt = ['Select rows', 'Drop rows']
        seldrop = widgets.Dropdown(
            options=sdopt, value=sdopt[0], description='Select/Drop: ')

        
        #display(seldrops)
        display(seldrop)
        display(vb)
        display(Hbb)
        ba.on_click(functools.partial(on_ba_clicked))
        #display(seldrop.value)
        #sel_val = 'Select rows'
        def res(cntrl):#'Select rows', 'Drop rows'
            student.flto  =1
            sel_val = seldrop.value
            #display(sel_val)
            #bs.on_click(functools.partial(on_bs_clicked, seldr = sel_val))
            return sel_val
        k = seldrop.observe(res, names = 'value')
        #res('a')
        if k == None:
            sel_val = 'Select rows'
        else:
            sel_val =  k
        r = widgets.RadioButtons(
            options=['Select rows', 'Drop rows'],

            description='Operation :',
            disabled=False
            )
        #display(r)
        #sel_val =  seldrop.value
        #display('*',sel_val)
        #if student.flto == 0:
        bs.on_click(functools.partial(on_bsf_clicked, seldr = seldrop.value))


    #######################################################################################################
    def change_dt_func(co_wid, tb=False):

        clear_output()
        x = co_wid
        clear_output()

        tb_val = tb
        head_buttons_disp(x, tb=tb_val,co = True)

        df = stu.dataf

        cd_dropdown_values = df.columns

        cdd_dropdown_values = [
            'str', 'object', 'int', 'float', 'bool'
        ]

        cd_dropdown = widgets.Dropdown(
            value=cd_dropdown_values[0],
            placeholder='Choose Someone',
            options=cd_dropdown_values,
            description='Column :',
            ensure_option=False,
            disabled=False)

        cdd_dropdown = widgets.Dropdown(
            value=cdd_dropdown_values[0],
            placeholder='Choose Someone',
            options=cdd_dropdown_values,
            description='Data type :',
            ensure_option=False)

        b_cdd = widgets.Button(description='Execute')
        b_cdd.style.button_color = 'green'

        def on_b_cdd_clicked(c):

            col = cd_dropdown.value

            #print(col)

            eval_st = 'df.{col_val}.astype'.format(col_val=cd_dropdown.value)
            eval_st += '({cdd_val})'.format(
                cdd_val=cdd_dropdown.value)
            try:
                df[col] = eval(eval_st)
            except:
                js = '<script>alert("Exception raised with the option selected, Please go BACK ");</script>';display(HTML(js));raise

            sq = '\''
            code_st = 'df[' + sq + '{col}'.format(col=col)

            code_st += sq + ']'

            student.code_list.append(code_st)

            student.code_list.append(eval_st)

            student.dataf = df

            clear_output()

            primary_disp()

        b_cdd.on_click(functools.partial(on_b_cdd_clicked))

        display(cd_dropdown)

        display(cdd_dropdown)

        display(b_cdd)


    #######################################################################################################
    def mc_func(co_wid, tb=False):

        clear_output()
        x = co_wid
        clear_output()

        tb_val = tb
        head_buttons_disp(x, tb=tb_val, co = True)

        df = student.dataf

        expa = df.columns
        ea = widgets.Dropdown(options=expa, value=expa[0], description='Move : ')

        expb = ['Move Before', 'Move After']
        eb = widgets.Dropdown(
            options=expb, value=expb[0], description='Condition: ')

        expac = df.columns
        eac = widgets.Dropdown(
            options=expac, value=expac[0], description='Column: ')

        bs = widgets.Button(description='Execute')
        bs.style.button_color = 'green'

        el_layout = Layout(width='2px', height='0px')
        el = widgets.Label("", Layout=el_layout)

        vb = VBox([ea, el, eb, el, eac, el, bs])
        display(vb)

        def on_bs_clicked(cntrl):

            df = student.dataf
            df_lis = list(df.columns)

            
            
            #i_ind =  df_lis.index(ea.value)
            
            
            
            #print(a[:ind]);print(a[ind:])
            
            if ea.value != eac.value:
                
                df_lis.remove(ea.value)
                
                ind = df_lis.index(eac.value)
                
                if eb.value == 'Move Before':
                    
                    df_lis =  df_lis[:ind] + [ea.value] + df_lis[ind:]
                    
                if eb.value == 'Move After':
                    df_lis =  df_lis[:ind+1] + [ea.value] + df_lis[ind+1:]
                

#                 if eb.value == 'Move Before':
#                     if i_ind == 0 and ind == 0:
#                         df_lis.insert(ind, ea.value)
#                     else:
#                         if ind!= 0:
#                             df_lis.insert(ind-1, ea.value)
#                         #else:
#                         #    df_lis.insert(ind-2, ea.value)
#                 if eb.value == 'Move After':
#                     df_lis.insert(ind, ea.value)

            eval_st = 'df[{cols}]'.format(cols=df_lis)
            try:
                df = eval(eval_st)
            except:
                js = '<script>alert("Exception raised with the option selected, Please go BACK ");</script>';display(HTML(js));raise

            student.code_list.append(eval_st)
            student.dataf = df
            primary_disp()

        bs.on_click(functools.partial(on_bs_clicked))


    #######################################################################################################
    def sort_func(co_wid, tb=False):

        clear_output()
        x = co_wid
        clear_output()

        
        tb_val = tb
#         if tb_val == True:
#             head_buttons_disp(x, tb=True, co = True)
#         else:
#             head_buttons_disp(x, tb=False, co = True)
        if tb_val == True:
            head_buttons_disp1(x)
        else:
            head_buttons_disp(x, tb=False, co = True)
        #head_buttons_disp1(x)
        el_layout = Layout(width='2px', height='0px')
        el = widgets.Label("", Layout=el_layout)

        flt_dict = dict()

        #stu1 = student()

        flt_dict['stu1'] = student()
        student.srt_cnt += 1

        key_val = flt_dict['stu1']

        ba = widgets.Button(description='Add Condition')
        ba.style.button_color = 'lightgray'

        bs = widgets.Button(description='Execute')
        bs.style.button_color = 'green'

        cs_dropdown = key_val.cs_dropdown

        css_dropdown = key_val.css_dropdown

        Hb1 = HBox([cs_dropdown, css_dropdown])
        vb = VBox([Hb1, el])
        display(vb)

        Hbb = HBox([ba, bs])
        display(Hbb)

        def select_cd(srt_val, expr_dict, flt_dict):
            df = student.dataf
            sq = '\''
            eval_st = 'df.sort_values(['

            for i in range(len(srt_val['cs_dropdown'])):

                eval_st += sq
                eval_st += '{srt_col}'.format(srt_col=srt_val['cs_dropdown'][i])
                eval_st += sq

                if i != len(srt_val['cs_dropdown']) - 1:
                    eval_st += ','

            eval_st += '], ascending = ['

            for i in range(len(srt_val['css_dropdown'])):

                eval_st += '{srt_col}'.format(
                    srt_col=expr_dict[srt_val['css_dropdown'][i]])

                if i != len(srt_val['css_dropdown']) - 1:
                    eval_st += ','

            eval_st += '])'
            try:
                df = eval(eval_st)
            except:
                js = '<script>alert("Exception raised with the option selected, Please go BACK ");</script>';display(HTML(js));raise

    #         for keys in flt_dict:

    #             st =  "del "+keys
    #             exec(st)

            student.dataf = df

            student.code_list.append(eval_st)

            primary_disp()

        def on_ba_clicked(cntrl):
            cnt = student.srt_cnt
            cnt = str(cnt)

            #el_layout = Layout(width='2px',height='2px')
            el = widgets.Label("")

            nxt_key = 'stu' + cnt

            flt_dict[nxt_key] = student()
            student.srt_cnt += 1

            nxt_key = flt_dict[nxt_key]

            cs_dropdown = nxt_key.cs_dropdown
            css_dropdown = nxt_key.css_dropdown

            Hb2 = HBox([cs_dropdown, css_dropdown])
            vb.children += (el, Hb2, el)

        def on_bs_clicked(cntrl):
            srt_val = dict()
            cs_dropdown_val = list()
            css_dropdown_val = list()

            for d_keys in flt_dict.keys():

                d_keys = flt_dict[d_keys]

                cs_dropdown_val.append(d_keys.cs_dropdown.value)
                css_dropdown_val.append(d_keys.css_dropdown.value)



            #display(ea_val, eb_val, tx_val)

            srt_val['cs_dropdown'] = cs_dropdown_val
            srt_val['css_dropdown'] = css_dropdown_val

            altr = [1, 0]

            expr = ['Ascending(A-Z)', 'Descending(Z-A)']

            expr_dict = dict()

            for i, j in zip(expr, altr):
                expr_dict[i] = j

            select_cd(srt_val, expr_dict, flt_dict)

        ba.on_click(functools.partial(on_ba_clicked))

        bs.on_click(functools.partial(on_bs_clicked))


    #######################################################################################################
    def sm_func(co_wid, tb=False):

        clear_output()
        x = co_wid
        clear_output()

        tb_val = tb
        head_buttons_disp(x, tb=tb_val, co = True)

        expa = ['Split string', 'Find and replace', 'Extract substring' , 'strip/trim space','to lowercase', 'to uppercase','length']
        ea =  widgets.Dropdown(options=expa,value=None, description='Select: ' )



        def response(cntrl):
            clear_output()
            head_buttons_disp(ea.value, co = True)
            display(ea)

            df = student.dataf

            #******************************
            if ea.value =='Split string':

                #head_buttons_disp(ea.value, co = True)

                cols_val = df.columns
                col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

                display(col)

                tx =  widgets.Text(description = 'Split string')

                display(tx)
                def on_bsplit_clicked(cntrl):
                    #df = pd.read_csv(r'C:\Users\thaarunn\Desktop\titanic.csv')
                    df =  student.dataf
                    name =  col.value
                    value =  tx.value
                    split_df = df[name].str.split(value, expand =  True) 

                    split_df.columns =[f"Name{id_}" for id_ in range(len(split_df.columns))]

                    #df =  pd.merge(df, split_df, how = 'left',left_index =True, right_index =  True)

                    student.splitdataf =  split_df
                    #eval_st =  'pd.merge(df, {split}, how =\'left\',left_index =True, right_index =  True)'.format(split =  student.splitdataf)
                    eval_st =  'pd.merge(df, split_df, how =\'left\',left_index =True, right_index =  True)'
                    try:
                        df = eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go BACK ");</script>';display(HTML(js));raise

                    student.dataf = df
                    student.code_list.append(eval_st)
                    primary_disp()

                bsplit = widgets.Button(description='Execute')
                bsplit.style.button_color = 'green'
                bsplit.on_click(functools.partial(on_bsplit_clicked))

                display(bsplit)

            #******************************
            if ea.value =='Find and replace':

                #head_buttons_disp(ea.value, co = True)
                #df['Name'] =  df['Name'].str.replace('B','BB')
                cols_val = df.columns
                col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

                display(col)

                tx =  widgets.Text(description = 'Find :')

                display(tx)

                txr =  widgets.Text(description = 'Replace :')

                display(txr)

                def on_bfr_clicked(cntlr):
                    #df['Name'] =  df['Name'].str.replace('B','BB')

                    sq  = '\''
                    code_st =  'df['+sq+'{col}'.format(col = col.value)
                    code_st += sq + ']'

                    eval_st =  'df['+sq+'{col}'.format(col = col.value)
                    eval_st +=  sq + '].str.replace(' + sq
                    eval_st +=  '{col}'.format(col =  tx.value)
                    eval_st +=  sq + ','+sq
                    eval_st +=  '{col}'.format(col =  txr.value)
                    eval_st +=  sq + ')'

                    key =  col.value

                    try:
                        df[key] =  eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go BACK ");</script>';display(HTML(js));raise

                    student.dataf = df
                    student.code_list.append(code_st)
                    student.code_list.append(eval_st)

                    primary_disp()

                bfr = widgets.Button(description='Execute')
                bfr.style.button_color = 'green'
                bfr.on_click(functools.partial(on_bfr_clicked))

                display(bfr)

            #******************************   
            if ea.value =='Extract substring': 
                #df['Name'] =  df['Name'].str.slice(start=1, stop = 5)
                #head_buttons_disp(ea.value, co = True)
                cols_val = df.columns
                col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

                display(col)

                tx =  widgets.Text(description = 'Start val')

                display(tx)

                txr =  widgets.Text(description = 'End val')

                display(txr)

                def on_bfr_clicked(cntlr):
                    #df['Name'] =  df['Name'].str.replace('B','BB')

                    sq  = '\''
                    code_st =  'df['+sq+'{col}'.format(col = col.value)
                    code_st += sq + ']'

                    eval_st =  'df['+sq+'{col}'.format(col = col.value)
                    eval_st +=  sq + '].str.slice(start ='
                    eval_st +=  '{col}'.format(col =  tx.value)
                    eval_st +=  ',stop = '
                    eval_st +=  '{col}'.format(col =  txr.value)
                    eval_st +=   ')'

                    key =  col.value
                    try:
                        df[key] =  eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                        
                    student.dataf = df
                    student.code_list.append(code_st)
                    student.code_list.append(eval_st)

                    primary_disp()

                bfr = widgets.Button(description='Execute')
                bfr.style.button_color = 'green'
                bfr.on_click(functools.partial(on_bfr_clicked))

                display(bfr)

            #******************************
            if ea.value =='strip/trim space':
                #head_buttons_disp(ea.value, co = True)
                #df['Name'] =  df['Name'].str.strip()
                cols_val = df.columns
                col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

                colss_val = ['strip','lstrip','rstrip']
                cols =  widgets.Dropdown(options=colss_val,value=colss_val[0], description='Func: ' )

                display(col)
                display(cols)

                def on_btr_clicked(cntrl):

                    sq  = '\''
                    code_st =  'df['+sq+'{col}'.format(col = col.value)
                    code_st += sq + ']'

                    eval_st =  'df['+sq+'{col}'.format(col = col.value)
                    eval_st +=  sq 
                    eval_st += '].str.{strip}()'.format(strip = cols.value)


                    key =  col.value
                    try:
                        df[key] =  eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                    student.dataf = df
                    student.code_list.append(code_st)
                    student.code_list.append(eval_st)

                    primary_disp()

                btr = widgets.Button(description='Execute')
                btr.style.button_color = 'green'
                btr.on_click(functools.partial(on_btr_clicked))

                display(btr)
            #******************************    
            if ea.value =='to lowercase':
                #head_buttons_disp(ea.value, co = True)
                #data["Team"]= data["Team"].str.upper() 
                cols_val = df.columns
                col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

                display(col)

                def on_btr_clicked(cntrl):

                    sq  = '\''
                    code_st =  'df['+sq+'{col}'.format(col = col.value)
                    code_st += sq + ']'

                    eval_st =  'df['+sq+'{col}'.format(col = col.value)
                    eval_st +=  sq 
                    eval_st += '].str.lower()'

                    key =  col.value
                    try:
                        df[key] =  eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                    student.dataf = df
                    student.code_list.append(code_st)
                    student.code_list.append(eval_st)

                    primary_disp()

                btr = widgets.Button(description='Execute')
                btr.style.button_color = 'green'
                btr.on_click(functools.partial(on_btr_clicked))

                display(btr)

            #******************************    
            if ea.value =='to uppercase':
                #head_buttons_disp(ea.value, co = True)
                #data["Team"]= data["Team"].str.lower() 
                #data["Team"]= data["Team"].str.upper() 
                cols_val = df.columns
                col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

                display(col)

                def on_btr_clicked(cntrl):

                    sq  = '\''
                    code_st =  'df['+sq+'{col}'.format(col = col.value)
                    code_st += sq + ']'

                    eval_st =  'df['+sq+'{col}'.format(col = col.value)
                    eval_st +=  sq 
                    eval_st += '].str.upper()'

                    key =  col.value
                    try:
                        df[key] =  eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                    student.dataf = df
                    student.code_list.append(code_st)
                    student.code_list.append(eval_st)

                    primary_disp()

                btr = widgets.Button(description='Execute')
                btr.style.button_color = 'green'
                btr.on_click(functools.partial(on_btr_clicked))

                display(btr)
            #******************************    
            if ea.value =='length':
                #head_buttons_disp(ea.value, co = True)
                #data["Team"]= data["Team"].str.upper() 
                cols_val = df.columns
                col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

                display(col)

                def on_btr_clicked(cntrl):

                    sq  = '\''
                    code_st =  'df['+sq+'{col}'.format(col = col.value)
                    code_st += sq + ']'

                    eval_st =  'df['+sq+'{col}'.format(col = col.value)
                    eval_st +=  sq 
                    eval_st += '].str.len()'

                    key =  col.value
                    try:
                        df[key] =  eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                    student.dataf = df
                    student.code_list.append(code_st)
                    student.code_list.append(eval_st)

                    primary_disp()

                btr = widgets.Button(description='Execute')
                btr.style.button_color = 'green'
                btr.on_click(functools.partial(on_btr_clicked))

                display(btr)


        ea.observe(response, names = 'value')
        display(ea)


    #######################################################################################################
    #######################################################################################################

    #Defining the contents of output(aout)
    with aout:

        clear_output()

        #Buttons delcaraion:
        bb = Button(description='Back', layout=bb_layout)
        bb.style.button_color = 'white'

        bcb = Button(description='Back', layout=bb_layout)
        bcb.style.button_color = 'white'

        bctb = Button(description='Back', layout=bb_layout)
        bctb.style.button_color = 'white'

        bh = Button(description='Head', layout=bh_layout, selected=True)
        bh.style.button_color = 'white'

        bt = Button(description='Show Table', layout=bt_layout)
        bt.style.button_color = 'white'

        btt = Button(description='Show Table', layout=bt_layout)
        btt.style.button_color = 'white'

        bc = Button(description='X', layout=bc_layout)
        bc.style.button_color = 'white'

        btc = Button(description='X', layout=bc_layout)
        btc.style.button_color = 'white'

        bs = Button(description='Select', button_style='Success')

        b_rname = Button(description='Rename', button_style='Success')

        #######################################################################################################


        def tabl_disp():

            qwidget_display, df_length = stu.get_qwidget()
            display(lineout)
            display(df_length)
            display(lineout)
            print('                                                     ' +
                  'Table View' + ' ')
            display(qwidget_display)

        #######################################################################################################

        def column_selected_disp(column_selected_val):

            display(column_selected_val)

        #######################################################################################################

        def summ_disp(column_summ_val):
            
            patho = eval('pd.__file__')
            patho =  patho.replace('pandas\__init__.py','')


            
            file = open(patho +"pandas_ui\plot.png", "rb")
            image = file.read()
            file1 = open(patho +"pandas_ui\plt1.png", "rb")
            image1 = file1.read()
            csv = widgets.Image(
                value=image,
                format='png',
                width=200,
                height=10, )
            csv1 = widgets.Image(
                value=image1,
                format='png',
                width=200,
                height=10, )

            display(lineout)
            print('            *****  ' + 'Summary' + '  *****')
            #print('')
            #display(column_summ_val)

            dist = Label('', layout=label_layout3)
            summ_hbox = widgets.HBox(
                [column_summ_val, dist, dist, csv1, dist, csv])
            display(summ_hbox)

        #######################################################################################################

        def hist_disp():

            display(lineout)
            print('            *****  ' + 'Distribution visualization' + '  *****')
            print(' ')
            stu.dig()

        #######################################################################################################
        def column_operations_disp():

            nc = ['filter', 'sort', 'change data type', 'move column']

            oc = [
                'string manipulations', 'filter', 'sort', 'change data type',
                'move column'
            ]

            dff = stu.dataf

            wid_value = stu.wid_value

            if dff.dtypes[wid_value] not in [object]:
                k = nc
            else:
                k = oc

            co_wid = widgets.Dropdown(
                options=k,
                value=None,
                description='Col Ops :',
                disabled=False,
                placeholde='Select Column Operation',
                layout=Layout(width='500px', height='30px'))

            def response(change):
                #co_wid =  co_wid.value
                if co_wid.value == 'filter':
                    filter_func(co_wid.value)

                if co_wid.value == 'change data type':
                    change_dt_func(co_wid.value)

                if co_wid.value == 'sort':
                    sort_func(co_wid.value)

                if co_wid.value == 'move column':
                    mc_func(co_wid.value)

                if co_wid.value == 'string manipulations':
                    sm_func(co_wid.value)

            co_wid.observe(response, names="value")

            display(co_wid)

        #######################################################################################################
        #######################################################################################################

        def on_b_r_button_clicked(b):

            if stu.r_name == 0:
                clear_output()
                primary_disp()
            else:
                x = 'rename'
                py_exec(x)

                clear_output()
                primary_disp()

        #######################################################################################################
        #Misselenous

        def on_b_r_button_clicked1(b, dff):
            def on_r_but_button_clicked(c):
                x = 'rename'
                tr = t_rname1.value
                py_exec(x, tr)

                #clear_output()
                #primary_disp()

            clear_output()
            head_buttons_disp(x='Rename')

            wid_value = student.wid_value

            t_rname = stu.textbox_func(
                value=wid_value,
                description='Old name :',
                placeholder='Enter New Name')
            #t_rname1 = stu.textbox_func(value =  'apple', description = 'New name :', placeholder = 'Enter New Name')

            t_rname1 = widgets.Text(
                value='apple',
                placeholder='Type something',
                description='String:',
                disabled=False)

            r_but = Button(description='Execute')

            r_but.on_click(functools.partial(on_r_but_button_clicked))

            display(t_rname)
            display(t_rname1)
            display(r_but)

        #######################################################################################################
        #Accordion changed widget
        def column_selected(br, tabslt=0):

            #Setting values for widget display

            wid_value = str(stu.wid.value)

            ##@ Changing class variable
            student.wid_value = wid_value

            #Displaying head
            head_buttons_disp(x=wid_value)

            t_rname = stu.textbox_func(
                value=wid_value,
                description='Rename :',
                placeholder='Enter New Name')

            def responsee(change):
                #display(t_rname.value)
                student.r_name = t_rname.value

            t_rname.observe(responsee, names='value')

            summ_out = stu.disp_summ()

            column_selected_val = HBox(
                [t_rname, Label('', layout=label_layout1), br])
            column_summ_val = HBox([Label('', layout=label_layout2), summ_out])

            #Calling fucntions to display widgets

            column_selected_disp(column_selected_val)

            column_operations_disp()

            print(" ")

            if tabslt == 1:
                tabl_disp()

            summ_disp(column_summ_val)

            hist_disp()

        #######################################################################################################
        def on_button_clicked(a, wid, br, dff):
            clear_output()
            column_selected(br)

        #######################################################################################################
        #######################################################################################################

        b1 = Button(
            description='Add Python Code',
            layout=Layout(flex='0.4 1 auto', width='auto'),
            button_style='')
        b2 = Button(
            description='Select/Drop columns',
            layout=Layout(flex='0.4 1 auto', width='auto'),
            button_style='')
        b3 = Button(
            description='Filter',
            layout=Layout(flex='0.3 1 auto', width='auto'),
            button_style='')
        b4 = Button(
            description='Sort',
            layout=Layout(flex='0.3 1 auto', width='auto'),
            button_style='')
        b5 = Button(
            description='New col formula',
            layout=Layout(flex='2.1 1 0%', width='auto'),
            button_style='')
        b6 = Button(
            description='Aggregate/Group',
            layout=Layout(flex='2.1 1 0%', width='auto'),
            button_style='')
        b7 = Button(
            description='Join',
            layout=Layout(flex='0.5 1 0%', width='auto'),
            button_style='')
        b8 = Button(
            description='Replace value',
            layout=Layout(flex='1.5 1 0%', width='auto'),
            button_style='')

        b9 = Button(
            description='Set/Update values',
            layout=Layout(flex='1 1 0%', width='50%'),
            button_style='')
        b10 = Button(
            description='OneHotEncoder',
            layout=Layout(flex='1 1 0%', width='auto'),
            button_style='')
        b11 = Button(
            description='Pivot',
            layout=Layout(flex='0.3 1 0%', width='auto'),
            button_style='')
        b12 = Button(
            description='Unpivot/Melt',
            layout=Layout(flex='0.6 1 0%', width='auto'),
            button_style='')
        b13 = Button(
            description='History',
            layout=Layout(flex='1 1 0%', width='auto'),
            button_style='success')
        #######################################################################################################

        arow = b1, b2, b3, b4, b5, b6, b7, b8

        items_1 = list(arow)

        brow = b9, b10, b11, b12, b13

        items_2 = list(brow)

        #######################################################################################################
        def on_b4_clicked(b1):

            sort_func(co_wid='Sort', tb=True)

        #######################################################################################################

        #Buttons invoking their functions
        b4.on_click(functools.partial(on_b4_clicked))

        #######################################################################################################


        def on_b3_clicked(b1):

            filter_func(co_wid='Filter', tb=True)

        #######################################################################################################

        #Buttons invoking their functions
        b3.on_click(functools.partial(on_b3_clicked))

        #######################################################################################################
        def on_b1_clicked(cntrl):

            clear_output()
            x = 'Code'
            clear_output()

            tb_val = True
            head_buttons_disp(x, tb=tb_val)

            df = student.dataf
            TA = widgets.Textarea(
                value='',
                placeholder='Enter code here',
                description='df =',
                disabled=False,
                rows=10,
                layout={'width': '800px'})

            display(TA)

            def on_b_ta_clicked(cntrl):
                df = student.dataf
                eval_st = '{TA}'.format(TA=TA.value)

                #sq = '\\' + '\''
                #eval_st = eval_st.replace('\'' ,sq)
                try:
                    df = eval(eval_st)
                except:
                    js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                student.dataf = df
                student.code_list.append(eval_st)

                primary_disp()

            b_ta = widgets.Button(description='Execute')
            b_ta.style.button_color = 'green'

            display(b_ta)

            b_ta.on_click(functools.partial(on_b_ta_clicked))

        #######################################################################################################

        #Buttons invoking their functions
        b1.on_click(functools.partial(on_b1_clicked))

        #######################################################################################################
        def on_b2_clicked(cntrl):
            def sel_mul(exp):
                clear_output()
                ex = widgets.Dropdown(
                    options=exp,
                    value=None,
                    description='Column(s): ', )

                def response(change):

                    sq = '\''
                    tx.value += sq + str(ex.value) + sq + ", "
                    display(ex.options)
                    temp_lis = [i for i in ex.options]

                    temp_lis.remove(ex.value)
                    opt = temp_lis
                    sel_mul(opt)

                ex.observe(response, names=["value", "options"])

                def on_bs_clicked(cntrl):
                    df =  student.dataf
                    tx.value = tx.value[:-2]

                    if col_ops_d.value == 'Select column(s)':
                        eval_st = 'df[[{cols}]]'.format(cols=tx.value)
                        try:
                            df = eval(eval_st)
                        except:
                            js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                    if col_ops_d.value == 'Drop column(s)':
                        eval_st = 'df.drop([{cols}], axis = 1)'.format(
                            cols=tx.value)
                        try:
                            df = eval(eval_st)
                        except:
                            js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                    student.dataf = df
                    student.code_list.append(eval_st)

                    primary_disp()

                bs = widgets.Button(description='Execute')
                bs.style.button_color = 'green'
                bs.on_click(functools.partial(on_bs_clicked))

                col_ops = ['Select column(s)', 'Drop column(s)']
                col_ops_d = widgets.Dropdown(
                    options=col_ops, value=col_ops[0], description='Select/Drop :')

                x = 'Select/Drop Column(s)'
                tb_val = True
                head_buttons_disp(x, tb=tb_val)

                Hbo = HBox([ex])
                display(Hbo)
                display(tx)
                display(col_ops_d)

                display(bs)

            tx = widgets.Text(
                description='Selected: ', placeholder='Selected values')
            df = student.dataf

            exp = df.columns
            sel_mul(exp)

        #######################################################################################################
        #Buttons invoking their functions
        b2.on_click(functools.partial(on_b2_clicked))

        #######################################################################################################
        def on_b11_clicked(cntrl):
            def sel_mul(exp):
                clear_output()
                ex = widgets.Dropdown(
                    options=exp,
                    value=None,
                    description='Column(s): ', )

                def response(change):

                    sq = '\''
                    tx.value += sq + str(ex.value) + sq + ", "
                    display(ex.options)
                    temp_lis = [i for i in ex.options]

                    temp_lis.remove(ex.value)
                    opt = temp_lis
                    sel_mul(opt)

                ex.observe(response, names=["value", "options"])

                def on_bs_clicked(cntrl):
                    tx.value = tx.value[:-2]
                    df =  student.dataf
                    #df.pivot(index = 'A', columns ='B', values = ['A'])

                    #eval_st  = 'df[[{cols}]]'.format(cols =  tx.value)
                    #df =  eval(eval_st)
                    sq = '\''
                    col_ops_dd = sq + col_ops_d.value + sq
                    if col_ops_i_d.value != None:
                        col_ops_i_dd = sq + col_ops_i_d.value + sq
                    else:
                        col_ops_i_dd = col_ops_i_d.value

                    eval_st = 'df.pivot(index ={val}'.format(val=col_ops_i_dd)
                    eval_st += ',columns = {val}'.format(val=col_ops_dd)
                    eval_st += ',values =[{val}])'.format(val=tx.value)
                    try:
                        df = eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                    student.pivotdf =  df
                    student.code_list.append(eval_st)
                    #student.dataff =  df
                    #student.get_temp_qwidget(df)
                    display(df)

                bs = widgets.Button(description='Execute')
                bs.style.button_color = 'green'
                bs.on_click(functools.partial(on_bs_clicked))

                col_ops = df.columns
                col_ops_d = widgets.Dropdown(
                    options=col_ops, value=col_ops[0], description='Variable :')

                col_ops_i = df.columns
                col_ops_i_d = widgets.Dropdown(
                    options=col_ops, value=None, description='Index :')

                x = 'Pivot'
                tb_val = True
                head_buttons_disp(x, tb=tb_val)

                Hbo = HBox([ex])
                display(Hbo)
                display(tx)
                display(col_ops_d)
                Hbo_lab = Label('* Optional')
                Hbo = HBox([col_ops_i_d, Hbo_lab])
                display(Hbo)
                display(bs)

            tx = widgets.Text(description='Selected: ', placeholder='bin')
            df = student.dataf

            exp = df.columns
            sel_mul(exp)

        #######################################################################################################

        #Buttons invoking their functions
        b11.on_click(functools.partial(on_b11_clicked))

        #######################################################################################################


        def on_b12_clicked(cntrl):
            #pd.melt(df, id_vars =['Name'], value_vars =['Course', 'Age'])
            #df = df.pivot(index = 'A', columns ='B', values = ['A'])

            def sel_mul(exp):
                clear_output()
                ex = widgets.Dropdown(
                    options=exp,
                    value=None,
                    description='value_vars: ', )

                def response(change):

                    sq = '\''
                    tx.value += sq + str(ex.value) + sq + ", "
                    display(ex.options)
                    temp_lis = [i for i in ex.options]

                    temp_lis.remove(ex.value)
                    opt = temp_lis
                    sel_mul(opt)

                ex.observe(response, names=["value", "options"])

                def on_bs_clicked(cntrl):
                    tx.value = tx.value[:-2]

                    #df.pivot(index = 'A', columns ='B', values = ['A'])
                    df = student.dataf
                    #eval_st  = 'df[[{cols}]]'.format(cols =  tx.value)
                    #df =  eval(eval_st)
                    sq = '\''
                    col_ops_dd = sq + col_ops_d.value + sq

                    eval_st = 'df.melt('
                    eval_st += 'value_vars = [{val}]'.format(val=tx.value)
                    eval_st += ',id_vars =[{val}])'.format(val=col_ops_dd)
                    try:
                        df = eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                    student.meltdf =  df
                    student.code_list.append(eval_st)
                    display(df)
                    #student.get_temp_qwidget(df)
                    #display(df)

                bs = widgets.Button(description='Execute')
                bs.style.button_color = 'green'
                bs.on_click(functools.partial(on_bs_clicked))

                col_ops = df.columns
                col_ops_d = widgets.Dropdown(
                    options=col_ops, value=col_ops[0], description='id_vars :')

                x = 'Unpivot/Melt'
                tb_val = True
                head_buttons_disp(x, tb=tb_val)

                Hbo = HBox([ex])
                display(Hbo)
                display(tx)
                display(col_ops_d)

                display(bs)

            tx = widgets.Text(description='Selected: ', placeholder='bin')
            df = student.dataf

            exp = df.columns
            sel_mul(exp)

        #######################################################################################################
        #Buttons invoking their functions
        b12.on_click(functools.partial(on_b12_clicked))

        #####################################################################################################
        def on_b5_clicked(cntrl):

            clear_output()
            x = 'New Column Formula'
            tb_val = True
            head_buttons_disp(x, tb=tb_val)

            TA = widgets.Textarea(
                value='',
                placeholder='Enter code here',
                description='Code :',
                disabled=False,
                rows=5,
                layout={'width': '800px'})

            col_name = widgets.Text(
                placeholder="Enter new column name", description="Name:")
            display(col_name)
            display(TA)

            def on_b_ta_clicked(cntrl):

                df = student.dataf
                display(TA.value)
                eval_st = '{TA}'.format(TA=TA.value)

                #sq = '\\' + '\''
                #eval_st = eval_st.replace('\'' ,sq)
                col_val = col_name.value
                try:
                    df[col_val] = eval(eval_st)
                except:
                    js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                    

                sq = '\''
                code_st = "df[" + sq + "{col}".format(col=col_val)

                code_st += sq + "]"

                student.code_list.append(code_st)

                student.code_list.append(eval_st)

                student.dataf = df

                primary_disp()

            b_ta = widgets.Button(description='Execute')
            b_ta.style.button_color = 'green'

            display(b_ta)

            b_ta.on_click(functools.partial(on_b_ta_clicked))

        #######################################################################################################
        #Buttons invoking their functions
        b5.on_click(functools.partial(on_b5_clicked))

        #####################################################################################################
        #df = pd.read_csv(r'C:\Users\thaarunn\Desktop\titanic.csv')
        def on_b10_clicked(cntrl):

            def sel_mul(exp):
                clear_output()
                ex = widgets.Dropdown(
                        options=exp,
                        value=None,
                        description='Column(s): ',

                    )



                def response(change):

                    sq = '\''
                    tx.value += sq+str(ex.value)+sq+ ", "
                    display(ex.options)
                    temp_lis =  [i for i in ex.options]

                    temp_lis.remove(ex.value)
                    opt = temp_lis
                    sel_mul(opt)


                ex.observe(response, names = ["value", "options"])

                def on_bs_clicked(cntrl):
                    tx.value =  tx.value[:-2]
                    #df =  pd.get_dummies(df,columns=['Sex'], drop_first = False, dummy_na=True)
                    df = student.dataf
                    eval_st = 'pd.get_dummies(df,columns=[{col}],'.format(col =tx.value)
                    eval_st += 'drop_first = {val},'.format(val = col_ops_d.value)
                    eval_st += 'dummy_na={val})'.format(val = col_opss_d.value)
                    try:
                        df =  eval(eval_st)
                    except:
                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                    #display(df)
                    student.dataf = df
                    student.code_list.append(eval_st)

                    primary_disp()


                bs = widgets.Button(description='Execute')
                bs.style.button_color = 'green'
                bs.on_click(functools.partial(on_bs_clicked))

                col_ops = [False,True]
                col_ops_d = widgets.Dropdown(options=col_ops,value=col_ops[0],description='drop_first :' )

                col_opss = [False,True]
                col_opss_d = widgets.Dropdown(options=col_ops,value=col_ops[0],description='dummy_na :' )

                x = 'One hot encoding'
                tb_val = True
                head_buttons_disp(x, tb=tb_val)

                Hbo = HBox([ex])
                display(Hbo)
                display(tx)
                display(col_ops_d)
                display(col_opss_d)

                display(bs)


            tx =  widgets.Text(description = 'Selected: ', placeholder ='bin')
            df = student.dataf

            exp= df.columns
            sel_mul(exp)
        #######################################################################################################

        #Buttons invoking their functions
        b10.on_click(functools.partial(on_b10_clicked))


        ###################################################################################################
        def on_b8_clicked(cntrl):
            clear_output()
            x = 'Find and Replace'
            tb_val = True
            head_buttons_disp(x, tb=tb_val)


            df =  student.dataf
            cols_val = df.columns
            col =  widgets.Dropdown(options=cols_val,value=cols_val[0], description='Column: ' )

            display(col)

            tx =  widgets.Text(description = 'Find :')

            display(tx)

            txr =  widgets.Text(description = 'Replace :')

            display(txr)

            def on_bfr_clicked(cntlr):
                #df['Name'] =  df['Name'].str.replace('B','BB')

                sq  = '\''
                code_st =  'df['+sq+'{col}'.format(col = col.value)
                code_st += sq + ']'

                eval_st =  'df['+sq+'{col}'.format(col = col.value)
                eval_st +=  sq + '].str.replace(' + sq
                eval_st +=  '{col}'.format(col =  tx.value)
                eval_st +=  sq + ','+sq
                eval_st +=  '{col}'.format(col =  txr.value)
                eval_st +=  sq + ')'

                key =  col.value

                try:
                    df[key] =  eval(eval_st)
                except:
                    js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                student.dataf = df
                student.code_list.append(code_st)
                student.code_list.append(eval_st)

                primary_disp()

            bfr = widgets.Button(description='Execute')
            bfr.style.button_color = 'green'
            bfr.on_click(functools.partial(on_bfr_clicked))

            display(bfr)
        #######################################################################################################

        #Buttons invoking their functions
        b8.on_click(functools.partial(on_b8_clicked))


        ###################################################################################################
        def on_b9_clicked(cntrl):
            def response(cntrl):


                if upd.value == 'Update table value':
                    clear_output()

                    x = 'Update table value';tb_val = True;head_buttons_disp(x, tb=tb_val)

                    display(lineout)
                    display(upd)
                    display(lineout)




                    def select_cd(dicto):


                        flt_val =  dicto
                        df = student.dataf



                        sq = '\''
                        temp_df = ""

                        int_dtypes = ['int','int8','int16','int32','int64']

                        flt_dtypes = ['float','float16','float32','float64']
                        #df = df.loc[df['Sex'].isin(['male']), 'Pclass'] = 5
                        #display(flt_val)
                        #['has value','contains','starts_with','ends_with','==','!=','>','<', '<=', '>=']
                        for i in range(len(flt_val['ea'])):

                            if df[flt_val['ea'][i]].dtype in int_dtypes:
                                flt_val['tx'][i] =  int(flt_val['tx'][i])

                            elif df[flt_val['ea'][i]].dtype in flt_dtypes:
                                flt_val['tx'][i] =  float(flt_val['tx'][i])

                            if flt_val['eo'][i] != None:
                                temp_df += ' ' + flt_val['eo'][i] + ' '

                            if flt_val['eb'][i] in ['==','!=','>','<', '<=', '>=']:
                                temp_df +=  '(df[\'{col}\']'.format(col = flt_val['ea'][i])
                                temp_df += '{cond}'.format(cond =  flt_val['eb'][i])
                                temp_df += '{val})'.format(val = flt_val['tx'][i])

                            else:
                                temp_df +=  '(df[\'{col}\']'.format(col = flt_val['ea'][i])
                                if flt_val['eb'][i] == 'has value':
                                    temp_df += '.isin([\'{val}\'])) '.format(val = flt_val['tx'][i])
                                else:
                                    temp_df += '.str.{cond}'.format(cond =  flt_val['eb'][i])
                                    temp_df += '(\'{val}\'))'.format(val = flt_val['tx'][i])

                        if toa.value != 'Null':
                            int_test = toa.value.isnumeric()
                            if int_test == True:
                                val =  int(toa.value)
                                #print('numeric')
                            else:
                                try :  
                                    float(test_string) 
                                    res = True
                                except : 
                                    res = False
                                if res == True:
                                    val =  float(toa.value)
                                    #print('float')
                                else:
                                    sq = '\''
                                    val = sq + toa.value + sq

                                    #print('str')


                        eval_st =  'df.loc[' + temp_df +',' + sq  + '{col}'.format(col = oa.value )
                        if toa.value != 'Null':
                            eval_st +=  sq + '] = {vals}'.format(vals = val)
                        else:
                            eval_st +=  sq + '] = np.nan'
                        #display(eval_st)
                        #display(df)



                        if els.value == True:
                            if toa2.value != 'Null':
                                int_test = toa2.value.isnumeric()
                                if int_test == True:
                                    val =  int(toa2.value)
                                    #print('numeric')
                                else:
                                    try :  
                                        float(test_string) 
                                        res = True
                                    except : 
                                        res = False
                                    if res == True:
                                        val =  float(toa2.value)
                                        #print('float')
                                    else:
                                        sq = '\''
                                        val = sq + toa2.value + sq

                                        #print('str')



                            eeval_st =  'df.loc[~(' + temp_df +'),' + sq  + '{col}'.format(col = oa2.value )




                            if toa2.value != 'Null':
                                eeval_st +=  sq + '] = {vals}'.format(vals = val)
                            else:
                                eeval_st +=  sq + '] = np.nan'

                            #display(eeval_st)
                            try:
                                exec(eeval_st)
                            except:
                                js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                            #student.dataf =  df
                            student.code_list.append(eeval_st)
                            #display(df)
                        try:
                            exec(eval_st)
                        except:
                            js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                        student.code_list.append(eval_st)

                        student.dataf = df

                        primary_disp()



                    altrlt = expb = ['!=','==','<=','>=', '>', '<']


                    flt_dict = dict()

                    stu1 = student()

                    flt_dict['stu1'] =  student()
                    student.upd_cnt += 1

                    key_val =  flt_dict['stu1']


                    el_layout = Layout(width='2px',height='0px')
                    el =  widgets.Label("",Layout = el_layout)

                    ea = key_val.aa
                    eb = key_val.ab
                    tx = key_val.ax
                    eo = key_val.ao



                    Hb1 = HBox([ea,eb,tx])
                    vb =  VBox([el,Hb1,el])
                    display(vb)

                    ba = widgets.Button(description='Add Condition')
                    ba.style.button_color = 'lightgray'
                    bs = widgets.Button(description='Execute')
                    bs.style.button_color = 'green'


                    Hbb =  HBox([ba, bs])
                    display(Hbb)


                    #display(ba)

                    oxpa = student.dataf.columns
                    oa =  widgets.Dropdown(options=oxpa,value=oxpa[0] )
                    l1 = Label('Set value of column')
                    #display(oa)
                    oxpaa = ['int', 'str' , 'float' ,  'Null']
                    oaa =  widgets.Dropdown(options=oxpaa,value=oxpaa[0] )
                    l2 = Label('dtype')

                    toa = widgets.Text(value = 'Null')
                    l3 = Label('To')

                    def response3(cntrl):
                        if oaa.value == 'Null':
                            toa.disabled = True
                        else:
                            toa.disabled = False

                    oaa.observe(response3, names = 'value')

                    v1 =  widgets.VBox([l1, oa])
                    v2 =  widgets.VBox([l2, oaa])
                    v3 =  widgets.VBox([l3, toa])

                    hoa = widgets.HBox([v1, v3])
                    display(hoa)
                    els_val = [False ,  True]
                    display(Label('Add else'))
                    els =  widgets.Dropdown(options=els_val,value=els_val[0])
                    #*********************
                    oxpa = student.dataf.columns
                    oa2 =  widgets.Dropdown(options=oxpa,value=oxpa[0] )

                    oxpaa = ['int', 'str' , 'float' ,  'Null']
                    oaa2 =  widgets.Dropdown(options=oxpaa,value=oxpaa[0] )
                    toa2 = widgets.Text(value = 'Null')

                    def response2(cntrl):
                        if oaa2.value == 'Null':
                            toa2.disabled = True
                        else:
                            toa2.disabled = False

                    oaa2.observe(response2, names = 'value')


                    #hoa2 = widgets.HBox([oaa2, toa])
                    l11= Label('Set value of column')
                    l22= Label('dtype')
                    l33= Label('To')


                    #*********************
                    def response(cntrl):
                        if els.value == True:
                            display(hoa2)
                            els.disabled = True

                    els.observe(response, names = 'value')

                    v11 =  widgets.VBox([l11, oa2])
                    v22 =  widgets.VBox([l22, oaa2])
                    v33 =  widgets.VBox([l33, toa2])
                    hoa2 = widgets.HBox([v11, v33])

                    display(els)




                    #display(bs)

                    def on_ba_clicked(cntrl):
                        cnt =  student.upd_cnt
                        cnt = str(cnt)

                        #el_layout = Layout(width='2px',height='2px')
                        el =  widgets.Label("")

                        nxt_key =  'stu' + cnt


                        flt_dict[nxt_key] =  student()
                        student.upd_cnt += 1

                        nxt_key = flt_dict[nxt_key]

                        ea =  nxt_key.aa
                        eb =  nxt_key.ab
                        tx =  nxt_key.ax
                        eo =  nxt_key.ao

                        Hb2 = HBox([ea,eb,tx])
                        vb.children += (eo, el ,Hb2, el)


                    def on_bs_clicked(cntrl):

                        flt_val = dict()
                        ea_val =  list()
                        eb_val =  list()
                        tx_val =  list()
                        eo_val =  list()

                        for d_keys in flt_dict.keys():

                            d_keys = flt_dict[d_keys]

                            ea_val.append(d_keys.aa.value)
                            eb_val.append(d_keys.ab.value)
                            tx_val.append(d_keys.ax.value)
                            eo_val.append(d_keys.ao.value)

                        #display(ea_val, eb_val, tx_val)

                        flt_val['ea'] =  ea_val
                        flt_val['eb'] =  eb_val
                        flt_val['tx'] =  tx_val
                        flt_val['eo'] =  eo_val



                        select_cd(flt_val)

                    stu =  student()
                    ba.on_click(functools.partial(on_ba_clicked))

                    bs.on_click(functools.partial(on_bs_clicked))

                else:
                    clear_output()
                    x = 'Handle Null value';tb_val = True;head_buttons_disp(x, tb=tb_val)
                    display(lineout)
                    display(upd)
                    display(lineout)

                    #*************************************************

                    oxpaa = ['Remove Null values' ,  'Fill Null values']
                    fd =  widgets.Dropdown(options=oxpaa,value=None , description = 'Operation: ')    


                    def resfd(cntl):

                        df =  student.dataf

                        if fd.value == 'Remove Null values': #,  'Fill Null values'

                            clear_output()
                            x = 'Remvoe';tb_val = True;head_buttons_disp(x, tb=tb_val)
                            display(lineout)
                            display(upd)
                            display(lineout)


                            display(fd)
                            oxpaa = ['Remove rows' ,  'Remove columns']
                            fd_val =  widgets.Dropdown(options=oxpaa,value=oxpaa[0] , description = 'Remove: ')

                            display(fd_val)
                            fdbn = widgets.Button(description='Execute')
                            fdbn.style.button_color = 'green'
                            def on_fdbn_clicked(cntrl):
                                #primary disp here:
                                df =  student.dataf
                                if fd_val.value == 'Remove rows':
                                    eval_st =  'df.dropna()'
                                    try:
                                        df = eval(eval_st)
                                    except:
                                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                                else:
                                    eval_st = 'df.dropna(axis =1)'
                                    try:
                                        df =  eval(eval_st)
                                    except:
                                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                                student.dataf =  df
                                student.code_list.append(eval_st)

                                primary_disp()

                            fdbn.on_click(functools.partial(on_fdbn_clicked))
                            display(fdbn)


                        else:
                            clear_output()
                            x = 'Fill';tb_val = True;head_buttons_disp(x, tb=tb_val)
                            display(lineout)
                            display(upd)
                            display(lineout)

                            display(fd)
                            oxpaa = ['All_columns'] + list(df.columns)
                            fd_val =  widgets.Dropdown(options=oxpaa,value= None , description = 'Column(s) :')
                            display(fd_val)
                            oxpaa_meth = ['Value' , 'Mean' , 'Median' , 'Frequent Value' , 'Forward Fill', 'Backward Fill']
                            fd_val_meth =  widgets.Dropdown(options=oxpaa_meth,value = None , description = 'Method :')
                            txfd = widgets.Text(description = 'Value :')
                            def fd_val_meth_res(cntl):
                                if fd_val_meth == 'Value':
                                    txfd.disabled =  True
                                if fd_val_meth != 'Value':
                                    txfd.disabled =  False

                            fd_val_meth.observe(fd_val_meth_res, names = 'value')

                            hfd = widgets.HBox([fd_val_meth, txfd])
                            display(hfd)
                            fdbn = widgets.Button(description='Execute')
                            fdbn.style.button_color = 'green'

                            def on_fdbn_clicked(cntl):
                                eval_st = ' '
                                df =  student.dataf
                                #print('$', fd_val.value)
                                if fd_val.value == 'All_columns':
                                    #print('inside')
                                    strin =  False
                                    if fd_val_meth.value == 'Value':
                                        int_test = txfd.value.isnumeric()
                                        if int_test == True:
                                            txfd_val =  int(txfd.value)
                                        else:
                                            try :  
                                                float(test_string) 
                                                res = True
                                            except : 
                                                res = False
                                            if res == True:
                                                txfd_val =  float(txfd.value)
                                            else:
                                                txfd_val = txfd.value
                                                strin = True


                                        eval_st += 'df.fillna('
                                        if strin == True:
                                            eval_st += '\'{vals}\')'.format(vals =  txfd_val)
                                        else:
                                            eval_st += '{vals})'.format(vals =  txfd_val)

                                    if fd_val_meth.value == 'Mean':
                                        eval_st +=  'df.fillna(df.mean())'
                                    if fd_val_meth.value == 'Median':
                                        eval_st +=  'df.fillna(df.median())'
                                    if fd_val_meth.value == 'Frequent Value':
                                        eval_st +=  'df.fillna(df.mode().iloc[0])'
                                    if fd_val_meth.value == 'Forward Fill':
                                        eval_st +=  'df.fillna(method = \'ffill\')'
                                    if fd_val_meth.value == 'Backward Fill':
                                        eval_st +=  'df.fillna(method = \'bfill\')'

                                    #display(eval_st)
                                    try:
                                        df =  eval(eval_st)
                                    except:
                                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                                    student.dataf =  df
                                    student.code_list.append(eval_st)
                                    df = 0
                                    primary_disp()

                                    #display(df)


                                if fd_val.value != 'All_columns':
                                    if fd_val_meth.value == 'Value':
                                        #print('inside value')
                                        strin = False
                                        int_test = txfd.value.isnumeric()
                                        if int_test == True:
                                            txfd_val =  int(txfd.value)
                                            #print('numeric')
                                        else:
                                            try :  
                                                float(test_string) 
                                                res = True
                                            except : 
                                                res = False
                                            if res == True:
                                                txfd_val =  float(txfd.value)
                                                #print('float')
                                            else:
                                                txfd_val = txfd.value
                                                strin = True
                                                #print('str')


                                        eval_st += 'df[\'{col}\'].fillna('.format(col =  fd_val.value)
                                        if strin == True:
                                            eval_st += '\'{vals}\')'.format(vals =  txfd_val)
                                        else:
                                            eval_st += '{vals})'.format(vals =  txfd_val)
                                            #display(eval_st)

                                    if fd_val_meth.value == 'Mean':
                                        eval_st +=  'df[\'{col}\'].fillna(df[\'{col}\'].mean())'.format(col =  fd_val.value)
                                    if fd_val_meth.value == 'Median':
                                        eval_st +=  'df[\'{col}\'].fillna(df[\'{col}\'].median())'.format(col =  fd_val.value)
                                    if fd_val_meth.value == 'Frequent Value':
                                        eval_st +=  'df[\'{col}\'].fillna(df[\'{col}\'].mode().iloc[0])'.format(col =  fd_val.value)
                                    if fd_val_meth.value == 'Forward Fill':
                                        eval_st +=  'df[\'{col}\'].fillna(method = \'ffill\')'.format(col =  fd_val.value)
                                    if fd_val_meth.value == 'Backward Fill':
                                        eval_st +=  'df[\'{col}\'].fillna(method = \'bfill\')'.format(col =  fd_val.value)

                                    code_st =  'df[\'{col}\']'.format(col =  fd_val.value)

                                    #print(code_st)
                                    cols_rvalue =  fd_val.value

                                    #display(eval_st)
                                    try:
                                        df[cols_rvalue] = eval(eval_st)
                                    except:
                                        js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                                    #eval(eval_st)
                                    ##display(df)
                                    student.code_list.append(code_st)
                                    student.dataf =  df
                                    student.code_list.append(eval_st)
                                    df = 0
                                    primary_disp()


                            fdbn.on_click(functools.partial(on_fdbn_clicked))
                            display(fdbn)


                    fd.observe(resfd, names = 'value')
                    display(fd)


                    #*************************************************

            lineout = widgets.Output(layout={'border': '1px solid black'})

            oxpaa = ['Update table value' ,  'Handle Null value']
            upd =  widgets.Dropdown(options=oxpaa,value=None , description = 'Operation: ')    

            upd.observe(response, names = 'value')
            clear_output()
            x ='Set/Update values';tb_val = True;head_buttons_disp(x, tb=tb_val)
            display(lineout)
            display(upd)
            display(lineout)


        ####################################################################################################

        #Buttons invoking their functions
        b9.on_click(functools.partial(on_b9_clicked))


        ###################################################################################################
        def on_b6_clicked(cntrl):
            def sel_mul(exp):
                clear_output()
                ex = widgets.Dropdown(
                        options=exp,
                        value=None,
                        description='Columns : ',
                                                 )

                def response(change):

                    sq = '\''
                    tx.value += sq+str(ex.value)+sq+ ", "
                    display(ex.options)
                    temp_lis =  [i for i in ex.options]

                    temp_lis.remove(ex.value)
                    opt = temp_lis
                    sel_mul(opt)


                ex.observe(response, names = ["value", "options"])

                x = 'Group by/Aggravate';tb_val = True;head_buttons_disp(x,tb=tb_val)
                el =  widgets.Label("")
                Hbo = HBox([ex])
                display(Hbo)
                display(tx)

                display(vb)

                display(Hbb)


            def select_cd(dicto):

                #flt_val =  dicto
                df = student.dataf
                
                tx_val =  tx.value
                tx_val =  tx_val[:-2]

                temp_df =  'df.groupby([{sel}]).agg('.format(sel =  tx_val)
                #print(temp_df)
                sq = '\''
                for i, j in zip(dicto['columns'],dicto['options']):
                    temp_df += i+"_"+j +" =("
                    temp_df += sq + i +sq +","+sq + j +sq + '),'
                temp_df =  temp_df[:-1]

                temp_df += ').reset_index()'
                display(temp_df)

                eval_st =  'df.merge('+temp_df+', on = [{sel}])'.format(sel = tx_val)
                try:
                    df =  eval(eval_st)
                except:
                    js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise
                #display(df)
                student.dataf =  df
                student.code_list.append(eval_st)
                student.grp_cnt = 1
                primary_disp()
                


            def on_ba_clicked(cntrl):

                cnt =  student.grp_cnt
                cnt = str(cnt)

                #el_layout = Layout(width='2px',height='2px')
                el =  widgets.Label("")

                nxt_key =  'stu' + cnt


                flt_dict[nxt_key] =  student()
                student.grp_cnt += 1

                nxt_key = flt_dict[nxt_key]

                ops  =  nxt_key.ops
                col  =  nxt_key.col

                Hb2 = HBox([ops, col])
                vb.children += (el,Hb2,el)



            def on_bs_clicked(cntrl):
                grp_val = dict()
                options_val =  list()
                columns_val =  list()

                for d_keys in flt_dict.keys():

                    d_keys = flt_dict[d_keys]

                    options_val.append(d_keys.ops.value)
                    columns_val.append(d_keys.col.value)

                #display(ea_val, eb_val, tx_val)

                grp_val['options'] =  options_val
                grp_val['columns'] =  columns_val

                display(grp_val)
                select_cd(grp_val)


            tx =  widgets.Text(description = 'Selected: ')
            df = student.dataf

            flt_dict = dict()

            flt_dict['stu1'] =  student()
            student.grp_cnt += 1

            key_val =  flt_dict['stu1']


            ops =  key_val.ops

            col = key_val.col

            Hb1 = HBox([ops,col])

            ba = widgets.Button(description='Add Condition')
            ba.style.button_color = 'lightgray'

            bs = widgets.Button(description='Execute')
            bs.style.button_color = 'green'

            ba.on_click(functools.partial(on_ba_clicked))
            bs.on_click(functools.partial(on_bs_clicked))

            Hbb =  HBox([ba, bs])

            vb =  VBox([Hb1])

            exp= df.columns
            sel_mul(exp)

        ####################################################################################################

        #Buttons invoking their functions
        b6.on_click(functools.partial(on_b6_clicked))


        ###################################################################################################
        def on_b7_clicked(cntrl):
            
            clear_output()
            x = 'Merge/Join';tb_val = True;head_buttons_disp(x,tb=tb_val)
            merge_val = ['inner','outer','left','right']
            merge =  widgets.Dropdown(options=merge_val,value=merge_val[0] )
            mlab =  Label('column:')
            mergo = widgets.HBox([mlab, merge])

            olab =  Label('Merge:   ')
            old_df =  widgets.Text(value = 'Current dataframe', disabled = True)
            nlab =  Label('  And  ')
            new_df =  widgets.Text(  placeholder = 'Enter path here')

            elab = Label(" ")

            btr = widgets.Button(description='Proceed')
            btr.style.button_color = 'gray'

            hm = widgets.HBox([olab, old_df, nlab, new_df,elab, btr])



            def on_btr_clicked(cntl):
                
                
                def sel_mul(exp, expr):

                    if exp == 'Null':
                        exp =  student.exp
                    else:
                        student.exp  =  exp

                    if expr == 'Null':
                        expr = student.expr
                    else:
                        student.expr =  expr


                    clear_output()



                    ex = widgets.Dropdown(
                            options=exp,
                            value=None,
                            description='Left_cols: ',

                        )


                    exr = widgets.Dropdown(
                            options=expr,
                            value=None,
                            description='Right_cols: ',

                        )



                    def response(change):

                        sq = '\''
                        tx.value += sq+str(ex.value)+sq+ ", "
                        display(ex.options)
                        temp_lis =  [i for i in ex.options]

                        temp_lis.remove(ex.value)
                        opt = temp_lis
                        sel_mul(exp = opt, expr = 'Null')


                    ex.observe(response, names = ["value", "options"])


                    def responser(change):

                        sq = '\''
                        txr.value += sq+str(exr.value)+sq+ ", "
                        display(ex.options)
                        temp_lis =  [i for i in exr.options]

                        temp_lis.remove(exr.value)
                        opt = temp_lis
                        sel_mul(expr = opt, exp = 'Null')


                    exr.observe(responser, names = ["value", "options"])

                    def on_bs_clicked(cntrl, df, dff):

            #             display(df)
            #             display(dff)
                        tx.value =  tx.value[:-2]
                        txr.value =  txr.value[:-2]
                        sq = '\''
                        eval_st = 'pd.merge(df,dff, how = '+sq+'{method}'.format(method = merge.value)
                        eval_st += sq +',left_on=[{l}], right_on = [{r}])'.format(l = tx.value, r = txr.value)

                        #print(eval_st)
                        try:
                            df =  eval(eval_st)
                        except:
                            js = '<script>alert("Exception raised with the option selected, Please go Back");</script>';display(HTML(js));raise

                        student.dataf =  df
                        student.code_list.append(eval_st)

                        primary_disp()
                        #display(result)


                    bs = widgets.Button(description='Execute')
                    bs.style.button_color = 'green'
                    bs.on_click(functools.partial(on_bs_clicked, df =  df, dff = dff))

                    col_ops = ['Select column(s)', 'Drop column(s)']
                    col_ops_d = widgets.Dropdown(options=col_ops,value=col_ops[0],description='Select/Drop :' )

                    x = 'Merge/Join';tb_val = True;head_buttons_disp(x,tb=tb_val)
                    Hbo = HBox([ex, tx])
                    Hbor = HBox([exr, txr])
                    display(mergo)
                    display(hm)

                    display(Hbo)
                    display(Hbor)
                    #display(tx)


                    display(bs)


                tx =  widgets.Text(description = 'On_left: ')
                txr =  widgets.Text(description = 'On_right: ')
                #df = pd.read_csv(r'C:\Users\thaarunn\Desktop\titanic.csv')
                #dff = pd.read_csv(r'C:\Users\thaarunn\Desktop\titanic.csv')

                df = student.dataf

                dff = pd.read_csv(new_df.value)
                Exp = list(df.columns)

                Expr= list(dff.columns)
                sel_mul(exp = Exp, expr = Expr)


            btr.on_click(functools.partial(on_btr_clicked))
            display(mergo)
            display(hm)


        ####################################################################################################

        #Buttons invoking their functions
        b7.on_click(functools.partial(on_b7_clicked))


        ###################################################################################################
        
        def on_b13_clicked(cntel):
            
            clear_output()
            x = 'History';tb_val = True;head_buttons_disp(x,tb=tb_val)
            
            
            student.org = student.code_list
    
            student.temp =  student.code_list

            
            bs = widgets.Button(description='Get_History',button_style='success')
            bundo = widgets.Button(description='Undo',button_style='warning',icon = 'fa-rotate-left')
            bredo = widgets.Button(description='Redo',button_style='info',icon = 'fa-rotate-right')
            bcommit = widgets.Button(description='Commit',button_style='success',icon = 'fa-anchor')

            #bs.style.button_color = 'green'
            #                    bs.on_click(functools.partial(o

            def displays():
                clear_output()

                x = 'History';tb_val = True;head_buttons_disp(x,tb=tb_val)

                #display(lineout)
                #display(head)
                #display(lineout)

                butts = widgets.HBox([bundo,bs, bredo, bcommit])
                display(butts)

                cnt = 0
                iterable = iter(student.temp)

                temp = student.temp


                for i in iterable:



                    ll = Label( ' ~ ')

                    if i[:7] == 'df.pivo' or i[:7] == 'df.melt' or i[:6] =='df.loc':
                        
                           
                            Lab = widgets.HTML(value="<b>"+i+"</b>")
        
                            hh = widgets.HBox([ll, Lab])
                            display(hh)

                    else:      

                        if i[:4] == 'df['+'\'' and i[-2:] == '\']':

                            #print('**', i[3:-1])
                            k = next(iterable)
                            i  = i + ' = '+ k
                            
                            Lab = widgets.HTML(value="<b>"+i+"</b>")
                            
                            hh = widgets.HBox([ll, Lab])
                            display(hh)
                            continue

                        else:
                            i =  'df = '+i
                            Lab = widgets.HTML(value="<b>"+i+"</b>")
                            hh = widgets.HBox([ll, Lab])
                            display(hh)

            def on_bundo_clicked(cntrl):

                temp = student.temp

                if len(temp) != 0:
                    pass
                    if len(temp) != 1:
                        sstr = temp[-2:-1][0]

                        if sstr[:4] == 'df['+'\'' and sstr[-2:] == '\']':

                            temp =  temp[:-2]

                        else:
                            temp = temp[:-1]
                    else:
                        temp = temp[:-1]

                student.temp =  temp        
                iterable = iter(student.temp)

                df = student.org_df
                for i in iterable:
                    if i[:7] == 'df.pivo' or i[:7] == 'df.melt':
                        pass
                    else:
                        if i[:6] =='df.loc':
                            exec(i)
                            student.dataff = df
                        else:
                            if i[:4] == 'df['+'\'' and i[-2:] == '\']':

                                col_val =  i[4:-2]
                                k = next(iterable)
                                df[col_val] =  eval(k)

                                continue

                            else:
                                df =  eval(i)




                student.dataff = df
                displays()




            def on_bredo_clicked(cntel):

                temp =  student.temp

                if len(student.temp) != len(student.org):

                    if student.org[len(student.temp)][:4] == 'df['+'\'' and student.org[len(student.temp)][-2:] == '\']':

                        student.temp.append(student.org[len(student.temp)])
                        student.temp.append(student.org[len(student.temp)])
                    else:
                        student.temp.append(student.org[len(student.temp)])

                else:
                    pass

                df = student.org_df
                iterable = iter(student.temp)

                for i in iterable:
                    if i[:7] == 'df.pivo' or i[:7] == 'df.melt':
                        pass
                    else:
                        if i[:6] =='df.loc':
                            exec(i)
                            student.dataff = df
                        else:   
                            if i[:4] == 'df['+'\'' and i[-2:] == '\']':

                                col_val =  i[4:-2]
                                k = next(iterable)
                                df[col_val] =  eval(k)

                                continue

                            else:
                                df =  eval(i)

                student.dataff = df
                displays()




            def on_bs_clicked(cntrl):
                displays()

                
            def on_bcommit_clicked(cntrl):
                student.code_list =  student.temp
                student.org = student.temp
                student.dataf =  student.dataff
                primary_disp()


            bs.on_click(functools.partial(on_bs_clicked))    

            bundo.on_click(functools.partial(on_bundo_clicked))


            bredo.on_click(functools.partial(on_bredo_clicked))
            
            bcommit.on_click(functools.partial(on_bcommit_clicked))



            lineout = widgets.Output(layout={'border': '1px solid black'})

            label_layout3 = Layout(width='200px', height='30px')

            head_label = Label('History')

            head = HBox([
                            Label('', layout=label_layout3),
                            Label('', layout=label_layout3),
                            bs,
                            Label('', layout=label_layout3),
                            Label('', layout=label_layout3)
                        ])
            butts = widgets.HBox([bundo,bs, bredo,bcommit])
            display(butts)
            displays()

            
        
        ##############################################################################

        #Buttons invoking their functions
        b13.on_click(functools.partial(on_b13_clicked))


        ###################################################################################################



        #item_1 = qwidget

        box_layout = Layout(
            height='35px',
            display='display',
            box_model='marigin',
            flex_flow='row',
            align_items='stretch',
            width='100%')

        box_layout_z = Layout(
            height='35px',
            display='display',
            box_model='marigin',
            flex_flow='row',
            align_items='stretch',
            width='70%')

        box_layout1 = Layout(
            height='80px',
            display='display',
            box_model='padding',
            flex_flow='column',
            align_items='stretch',
            width='95%')

        dflength = widgets.Label(
            value=str(df.shape[0]) + ' rows * ' + str(df.shape[1]) + ' Columns')

        box_1 = Box(children=items_1, layout=box_layout)

        box_2 = Box(children=items_2, layout=box_layout_z)

        box_z = Box(children=[box_1, box_2], layout=box_layout1)

        #######################################################################################################
        #######################################################################################################
        def primary_disp():
            #disp_accordion_val()
            clear_output()
            
            display(box_z)
            display(lineout)
            print('')
            wid = stu.cls_dropdown_func()
            accordion_val = HBox([
                Label('', layout=label_layout), wid,
                Label('', layout=label_layout1), bs
            ])

            def response(change):
                student.wid_value = wid.value

            wid.observe(response, names="value")
            display(accordion_val)
            display(lineout)
            qwidget_display, df_length = stu.get_qwidget()
            display(df_length)
            display(lineout)
            print('                                                     ' +
                  'Table View' + ' ')
            display(qwidget_display)

        #######################################################################################################
        def on_bc_clicked(d):
            student.flt_cnt = 1
            student.upd_cnt = 1
            clear_output()
            primary_disp()

        #######################################################################################################
        def on_bcb_clicked(d, br):
            student.flt_cnt = 1
            student.upd_cnt = 1
            clear_output()
            column_selected(br)

        #######################################################################################################
        def on_bb_clicked(e):
            clear_output()
            primary_disp()

        #######################################################################################################
        def on_bt_clicked(c, wid, br, dff):

            clear_output()
            column_selected(br, tabslt=1)

        #######################################################################################################
        def on_btc_clicked(c):

            clear_output()
            #tab_out_disp(accordion)
            primary_disp()

        #######################################################################################################

        #Buttons invoking their functions
        bs.on_click(
            functools.partial(on_button_clicked, wid=wid, br=b_rname, dff=df))

        #b_rname.on_click(functools.partial(on_b_r_button_clicked1, dff = df))
        b_rname.on_click(functools.partial(on_b_r_button_clicked))

        bt.on_click(functools.partial(on_bt_clicked, wid=wid, br=b_rname, dff=df))

        bc.on_click(functools.partial(on_bc_clicked))

        bb.on_click(functools.partial(on_bc_clicked))

        bcb.on_click(functools.partial(on_bcb_clicked, br=b_rname))

        bctb.on_click(functools.partial(on_btc_clicked))

        btc.on_click(functools.partial(on_btc_clicked))

        #######################################################################################################
        #Accordian init widget items
        #def disp_accordion_val():

        #disp_accordion_val()
        primary_disp()

    #######################################################################################################
    #Accordion:

    stu.stu_out = aout
    accordion = widgets.Accordion(children=[aout]
                                  #,selected_index = None
                                  )

    accordion.set_title(0, 'Magic')

    ########################################################################################################


    def tab_out_disp(accordion):

        df = stu.dataf
        aout = stu.stu_out
        accordion = widgets.Accordion(children=[aout]
                                      #,selected_index = None
                                      )

        accordion.set_title(0, 'Magic')

        clear_output()
        #display(box_z)
        #display(accordion)
        primary_disp()


    #######################################################################################################

    # v0 = VBox([Email()])
    # v1 = VBox([box_z])
    # v2 = VBox([accordion])

    #for  i in range(0, 3):
    #    disp_val = 'v' + str(i)
    #    exec('display(' + disp_val + ')')

    #######################################################################################################
    #######################################################################################################

    tab = widgets.Tab()

    tab_out = widgets.Output()

    with tab_out:
        tab_out_disp(accordion)

    #tab_c1 = VBox([box_z, accordion])
    tab_c1 = tab_out

    tab_c2 = widgets.Output()


    with tab_c2:
        bss = widgets.Button(description='Get_Profile',button_style='success')
        #bss.style.button_color = 'green'
        #                    bs.on_click(functools.partial(o
        def on_bss_clicked(cntrl):
            temp =  student.code_list
            clear_output()
            display(lineout)
            display(heads)
            display(lineout)
            display('Profile Report Processing...')
            df =  student.dataf
            prof = pp.ProfileReport(df)
            ppr = prof.to_notebook_iframe()
            display(ppr)






        bss.on_click(functools.partial(on_bss_clicked))

        lineout = widgets.Output(layout={'border': '1px solid black'})

        label_layout35 = Layout(width='200px', height='30px')

        #head_label = Label('History')

        heads = HBox([
                        Label('', layout=label_layout35),
                        Label('', layout=label_layout35),
                        bss,
                        Label('', layout=label_layout35),
                        Label('', layout=label_layout35)
                    ])
        display(lineout)
        display(heads)
        display(lineout)

    tab_c4 =  widgets.Output()
    with tab_c4:
        
        bcmd = widgets.Button(description='Commands',button_style='success')
        def on_bcmd_clicked(antrl):
            clear_output()
            
            display(lineout)
            display(headcmd)
            display(lineout)

            patho = eval('pd.__file__')
            patho =  patho.replace('pandas\__init__.py','')
            patho =  patho+'pandas_ui\panda.html'
            file = open(patho, "rb")
            image = file.read()
            htm = widgets.HTML(
                 value=image

             )
            display(htm)

        
        bcmd.on_click(functools.partial(on_bcmd_clicked))
        label_layout37 = Layout(width='200px', height='30px')

        

        headcmd = HBox([
                        Label('', layout=label_layout37),
                        Label('', layout=label_layout37),
                        bcmd,
                        Label('', layout=label_layout37),
                        Label('', layout=label_layout37)
                    ])
        display(lineout)
        display(headcmd)
        display(lineout)

        
    tab_c3 = widgets.Output()

    with tab_c3:

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        df = student.dataf

        plt_dig_opt = ['scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories']

        plt_dig = widgets.Dropdown(value=None,options=plt_dig_opt,description='Figure Type:')

        ###########################################################################################################
        def plt_response(cntrl):


            clear_output()
            display(plt_head)
            display(plt_slt)
            df = student.dataf
            #####################################################################################
            def plt_dd_creator(opts, desc):
                return widgets.Dropdown(value=None,options=opts,description=desc)

            plt_types = ['scatt','box','vio','hist','strip', 'area','dc','dh']

            plt3_types = ['scatt3','line3']

            plt3_vals = ['x','y','z','color','symb','size','ld']

            plt_vals = ['x','y','color','f_row','f_col','n_hov','symb','size']

            plt_ori_types = ['box','vio','hist','strip', 'area','dc','dh']
            plt_tx_vals  = ['title','x_min','x_max','y_min','y_max']
            plt3_tx_vals  = ['title','x_min','x_max','y_min','y_max','z_min','z_max']

            pltm_types = ['scatt_m','p_cat','p_coor']

            plt_tf_vals = [ 'log_x','log_y']
            plt3_tf_vals = [ 'log_x','log_y','log_z']

            plt_mar_types = ['scatt','dc','dh']
            plt_mar_vals = [ 'mar_x','mar_y']

            plt_wid_dict = dict()


            for types in plt_mar_types:
                for vals in plt_mar_vals:
                    plt_wid_dict[types+"_"+vals] =  plt_dd_creator(opts = ['rug','histogram','violin','box'], desc =types+"_"+vals )

            for types in plt3_types:
                for vals in plt3_tf_vals:
                    plt_wid_dict[types+"_"+vals] =  plt_dd_creator(opts = [True,False], desc =types+"_"+vals )


            for types in plt3_types:
                for vals in plt3_vals:
                    plt_wid_dict[types+"_"+vals] =  plt_dd_creator(opts = df.columns, desc =types+"_"+vals )


            for types in plt3_types:
                for vals in plt3_tx_vals:
                    plt_wid_dict[types+"_"+vals] =  widgets.Text(description =types+"_"+vals )


            for vals in plt_types:
                plt_wid_dict[vals+"_d_hov"] =  plt_dd_creator(opts = ["All columns"] , desc =vals+"_d_hov" )


            for vals in pltm_types:
                plt_wid_dict[vals+"_dim"] =  plt_dd_creator(opts = ["All columns"] + list(df.columns), desc =vals+"_dim" )

            for vals in pltm_types:
                plt_wid_dict[vals+"_color"] =  plt_dd_creator(opts = df.columns, desc =vals+"_color" )

            for vals in pltm_types:
                plt_wid_dict[vals+"_title"] =  widgets.Text(description =  vals+"_title")

            plt_wid_dict['scatt_m_sym'] =  plt_dd_creator(opts = df.columns, desc ='scatt_m_sym' )

            plt_wid_dict['scatt_m_size'] =  plt_dd_creator(opts = df.columns, desc ='scatt_m_size' )

            plt_wid_dict["scatt_m_n_hov"] =  plt_dd_creator(opts = df.columns, desc ="scatt_m_n_hov" )

            plt_wid_dict["scatt_m_d_hov"] =  plt_dd_creator(opts = ["All columns"], desc ="scatt_m_d_hov" )

            plt_wid_dict['scatt_m_s_max'] =  widgets.Text(description =  'scatt_m_s_max')

            for types in plt_types:
                for vals in plt_vals:
                    plt_wid_dict[types+"_"+vals] =  plt_dd_creator(opts = df.columns, desc =types+"_"+vals )


            for types in plt_types:
                for vals in plt_tf_vals:
                    plt_wid_dict[types+"_"+vals] =  plt_dd_creator(opts = [True,False], desc =types+"_"+vals )

            for vals in plt_ori_types:
                plt_wid_dict[vals+"_ori"] =  plt_dd_creator(opts = ["v","h"], desc =vals+"_ori" )

            for types in plt_types:
                for vals in plt_tx_vals:
                    plt_wid_dict[types+"_"+vals] =  widgets.Text(description =types+"_"+vals )


            plt_wid_dict['box_notch'] = plt_dd_creator(opts = [True,False], desc ='box_notch' )

            plt_wid_dict['vio_box'] = plt_dd_creator(opts = [True,False], desc ='violin_box')

            plt_wid_dict['hist_marg'] =  plt_dd_creator(opts = ['rug','histogram','violin','box'], desc ='hist_marg' )       


            plt_wid_dict['scatt_s_max'] =  widgets.Text(description =  'scatt_s_max')

            plt_wid_dict['hist_nbins'] =  widgets.Text(description =  'hist_nbins')

            lineout = widgets.Output(layout={'border': '1px solid black'})

            pw = plt_wid_dict


            lo = Label('* Optional')
            lo_h = widgets.VBox([lo, lineout])
            #########################################################################################################


           #############################################################################################
            if plt_dig.value == "scatter":
                scatt_h1 =  widgets.HBox([pw['scatt_x'],pw['scatt_y']])
                scatt_h2 =  widgets.HBox([pw['scatt_title'],pw['scatt_color']])
                scatt_h3 =  widgets.HBox([pw['scatt_x_min'],pw['scatt_x_max'],pw['scatt_y_min'],pw['scatt_y_max']])
                scatt_h4 =  widgets.HBox([pw['scatt_f_row'],pw['scatt_f_col'],pw['scatt_n_hov'],pw['scatt_d_hov']])
                scatt_h5 =  widgets.HBox([pw['scatt_log_x'],pw['scatt_log_y'],pw['scatt_size'],pw['scatt_symb']])
                scatt_h6 = widgets.HBox([pw['scatt_mar_x'],pw['scatt_mar_y'],pw['scatt_s_max']])

                display(scatt_h1,lo_h,scatt_h2,scatt_h3,scatt_h4,scatt_h5,scatt_h6)

            if plt_dig.value == "box":
                box_h1 =  widgets.HBox([pw['box_x'],pw['box_y']])
                box_h2 =  widgets.HBox([pw['box_title'],pw['box_color']])
                box_h3 =  widgets.HBox([pw['box_x_min'],pw['box_x_max'],pw['box_y_min'],pw['box_y_max']])
                box_h4 =  widgets.HBox([pw['box_f_row'],pw['box_f_col'],pw['box_n_hov'],pw['box_d_hov']])
                box_h5 =  widgets.HBox([pw['box_log_x'],pw['box_log_y'],pw['box_ori'],pw['box_notch']])

                display(box_h1,lo_h,box_h2,box_h3,box_h4,box_h5)

            if plt_dig.value == "violin":
                vio_h1 =  widgets.HBox([pw['vio_x'],pw['vio_y']])
                vio_h2 =  widgets.HBox([pw['vio_title'],pw['vio_color']])
                vio_h3 =  widgets.HBox([pw['vio_x_min'],pw['vio_x_max'],pw['vio_y_min'],pw['vio_y_max']])
                vio_h4 =  widgets.HBox([pw['vio_f_row'],pw['vio_f_col'],pw['vio_n_hov'],pw['vio_d_hov']])
                vio_h5 =  widgets.HBox([pw['vio_log_x'],pw['vio_log_y'],pw['vio_ori'],pw['vio_box']])

                display(vio_h1,lo_h,vio_h2,vio_h3,vio_h4,vio_h5)

            if plt_dig.value == "histogram":

                hist_h1 =  widgets.HBox([pw['hist_x'],pw['hist_y']])
                hist_h2 =  widgets.HBox([pw['hist_title'],pw['hist_color'],pw['hist_nbins']])
                hist_h3 =  widgets.HBox([pw['hist_x_min'],pw['hist_x_max'],pw['hist_y_min'],pw['hist_y_max']])
                hist_h4 =  widgets.HBox([pw['hist_f_row'],pw['hist_f_col'],pw['hist_n_hov'],pw['hist_d_hov']])
                hist_h5 =  widgets.HBox([pw['hist_log_x'],pw['hist_log_y'],pw['hist_ori'],pw['hist_marg']])

                display(hist_h1,lo_h,hist_h2,hist_h3,hist_h4,hist_h5)

            if plt_dig.value == "strip":
                strip_h1 =  widgets.HBox([pw['strip_x'],pw['strip_y']])
                strip_h2 =  widgets.HBox([pw['strip_title'],pw['strip_color']])
                strip_h3 =  widgets.HBox([pw['strip_x_min'],pw['strip_x_max'],pw['strip_y_min'],pw['strip_y_max']])
                strip_h4 =  widgets.HBox([pw['strip_f_row'],pw['strip_f_col'],pw['strip_n_hov'],pw['strip_d_hov']])
                strip_h5 =  widgets.HBox([pw['strip_log_x'],pw['strip_log_y'],pw['strip_ori']])

                display(strip_h1,lo_h,strip_h2,strip_h3,strip_h4,strip_h5)


            if plt_dig.value == "area":
                area_h1 =  widgets.HBox([pw['area_x'],pw['area_y']])
                area_h2 =  widgets.HBox([pw['area_title'],pw['area_color']])
                area_h3 =  widgets.HBox([pw['area_x_min'],pw['area_x_max'],pw['area_y_min'],pw['area_y_max']])
                area_h4 =  widgets.HBox([pw['area_f_row'],pw['area_f_col'],pw['area_n_hov'],pw['area_d_hov']])
                area_h5 =  widgets.HBox([pw['area_log_x'],pw['area_log_y'],pw['area_ori']])

                display(area_h1,lo_h,area_h2,area_h3,area_h4,area_h5)

            if plt_dig.value == "density_contour":
                dc_h1 =  widgets.HBox([pw['dc_x'],pw['dc_y']])
                dc_h2 =  widgets.HBox([pw['dc_title'],pw['dc_color']])
                dc_h3 =  widgets.HBox([pw['dc_x_min'],pw['dc_x_max'],pw['dc_y_min'],pw['dc_y_max']])
                dc_h4 =  widgets.HBox([pw['dc_f_row'],pw['dc_f_col'],pw['dc_n_hov'],pw['dc_d_hov']])
                dc_h5 =  widgets.HBox([pw['dc_log_x'],pw['dc_log_y']])
                dc_h6 = widgets.HBox([pw['dc_mar_x'],pw['dc_mar_y']])

                display(dc_h1,lo_h,dc_h2,dc_h3,dc_h4,dc_h5,dc_h6)



            if plt_dig.value == "density_heatmap" :

                dh_h1 =  widgets.HBox([pw['dh_x'],pw['dh_y']])
                dh_h2 =  widgets.HBox([pw['dh_title'],pw['dh_color']])
                dh_h3 =  widgets.HBox([pw['dh_x_min'],pw['dh_x_max'],pw['dh_y_min'],pw['dh_y_max']])
                dh_h4 =  widgets.HBox([pw['dh_f_row'],pw['dh_f_col'],pw['dh_n_hov'],pw['dh_d_hov']])
                dh_h5 =  widgets.HBox([pw['dh_log_x'],pw['dh_log_y']])
                dh_h6 = widgets.HBox([pw['dh_mar_x'],pw['dh_mar_y']])

                display(dh_h1,lo_h,dh_h2,dh_h3,dh_h4,dh_h5,dh_h6)

            if plt_dig.value == "scatter_3d":

                scatt3_h1 =  widgets.HBox([pw['scatt3_x'],pw['scatt3_y'],pw['scatt3_z']])
                scatt3_h2 =  widgets.HBox([pw['scatt3_title'],pw['scatt3_color']])
                scatt3_h3 =  widgets.HBox([pw['scatt3_log_x'],pw['scatt3_log_y'],pw['scatt3_log_z']])
                scatt3_h4 =  widgets.HBox([pw['scatt3_x_min'],pw['scatt3_x_max'],pw['scatt3_y_min'],pw['scatt3_y_max']])
                scatt3_h5 =  widgets.HBox([pw['scatt3_z_min'],pw['scatt3_z_max'],pw['scatt3_symb'],pw['scatt3_size']])

                display(scatt3_h1,lo_h,scatt3_h2,scatt3_h3,scatt3_h4,scatt3_h5)

            if plt_dig.value == "line_3d":

                line3_h1 =  widgets.HBox([pw['line3_x'],pw['line3_y'],pw['line3_z']])
                line3_h2 =  widgets.HBox([pw['line3_title'],pw['line3_color']])
                line3_h3 =  widgets.HBox([pw['line3_log_x'],pw['line3_log_y'],pw['line3_log_z']])
                line3_h4 =  widgets.HBox([pw['line3_x_min'],pw['line3_x_max'],pw['line3_y_min'],pw['line3_y_max']])
                line3_h5 =  widgets.HBox([pw['line3_z_min'],pw['line3_z_max'],pw['line3_ld']])



                display(line3_h1,lo_h,line3_h2,line3_h3,line3_h4,line3_h5)
            #'scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'
            if plt_dig.value == "parallel_categories":

                p_cat_h1 =  widgets.HBox([pw['p_cat_title'],pw['p_cat_color']])
                #p_cat_h2 =  widgets.HBox([pw['p_cat_dim']])

                display(lo_h,p_cat_h1)

            if plt_dig.value == "parallel_coordinates":

                p_coor_h1 =  widgets.HBox([pw['p_coor_title'],pw['p_coor_color']])
                #p_coor_h2 =  widgets.HBox([pw['p_coor_dim']])

                display(lo_h,p_coor_h1)

            if plt_dig.value == "scatter_matrix":

                scatt_m_h1 =  widgets.HBox([pw['scatt_m_title'],pw['scatt_m_color']])
                scatt_m_h2 =  widgets.HBox([pw['scatt_m_n_hov'],pw['scatt_m_d_hov']])
                scatt_m_h3 =  widgets.HBox([pw['scatt_m_sym'],pw['scatt_m_size'],pw['scatt_m_s_max']])

                display(lo_h,scatt_m_h1,scatt_m_h2, scatt_m_h3)

            #print('hai')

            def on_bplt_clicked(cntrl):
                #widgs()
                sq = '\''
                clear_output()
                df =  student.dataf





                if plt_dig.value == "scatter":

                    if pw['scatt_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['scatt_x'].value + sq

                    if pw['scatt_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['scatt_log_x'].value 

                    if pw['scatt_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['scatt_log_y'].value 

                    if pw['scatt_mar_x'].value == None:
                        marxx = None
                    else:
                        marxx =  sq + pw['scatt_mar_x'].value + sq

                    if pw['scatt_mar_y'].value == None:
                        maryx = None
                    else:
                        maryx =  sq + pw['scatt_mar_y'].value + sq

                    if pw['scatt_symb'].value == None:
                        symbx = None
                    else:
                        symbx =  sq + pw['scatt_symb'].value + sq

                    if pw['scatt_size'].value == None:
                        sizex = None
                    else:
                        sizex =  sq + pw['scatt_size'].value + sq


                    if pw['scatt_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['scatt_y'].value + sq

                    if pw['scatt_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['scatt_title'].value + sq

                    if pw['scatt_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['scatt_color'].value + sq

                    if pw['scatt_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['scatt_f_row'].value + sq

                    if pw['scatt_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['scatt_f_col'].value + sq


                    if pw['scatt_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['scatt_n_hov'].value + sq


                    if pw['scatt_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['scatt_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)



                    if pw['scatt_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['scatt_x_min'].value), int(pw['scatt_x_max'].value)]
                    if pw['scatt_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['scatt_y_min'].value), int(pw['scatt_y_max'].value)]
                    if pw['scatt_s_max'].value == "":
                        size_maxx =  None
                    else:
                        size_maxx  = int(pw['scatt_s_max'].value)



                    plt_st = "px.scatter(df,    x = {x} ,     y = {y},  title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} ,  facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name},    size={size},      symbol = {symbol}, marginal_x = {marginal_x},        marginal_y={marginal_y},   hover_data = {hover_data},  size_max={size_max})".format(x = xx,    y = yx,      title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,      range_x =rangexx , range_y = rangeyy ,      facet_row = f_rowx,   facet_col =f_colx,    hover_name =n_hovx , hover_data=d_hovx,        size = sizex,          symbol =symbx ,     marginal_x =marxx ,     marginal_y =maryx ,   size_max = size_maxx )

                    fig = eval(plt_st)
                #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "box":

                    if pw['box_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['box_x'].value + sq

                    if pw['box_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['box_log_x'].value 

                    if pw['box_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['box_log_y'].value 




                    if pw['box_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['box_y'].value + sq

                    if pw['box_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['box_title'].value + sq

                    if pw['box_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['box_color'].value + sq

                    if pw['box_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['box_f_row'].value + sq

                    if pw['box_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['box_f_col'].value + sq


                    if pw['box_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['box_n_hov'].value + sq

                    if pw['box_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['box_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)




                    if pw['box_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['box_x_min'].value), int(pw['box_x_max'].value)]
                    if pw['box_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['box_y_min'].value), int(pw['box_y_max'].value)]


                    if pw['box_ori'].value == None:
                        orix = None
                    else:
                        orix =  sq + pw['box_ori'].value + sq




                    plt_st = "px.box(df,    x = {x} ,     y = {y},  title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} ,  facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name},hover_data = {hover_data}, orientation = {orientation},notched = {notched})".format(x = xx,    y = yx,      title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,      range_x =rangexx , range_y = rangeyy ,      facet_row = f_rowx,   facet_col =f_colx,  hover_data = d_hovx,  hover_name =n_hovx   , orientation = orix, notched = pw['box_notch'].value)

                    fig = eval(plt_st)

                    #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "violin":

                    if pw['vio_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['vio_x'].value + sq

                    if pw['vio_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['vio_log_x'].value 

                    if pw['vio_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['vio_log_y'].value 




                    if pw['vio_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['vio_y'].value + sq

                    if pw['vio_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['vio_title'].value + sq

                    if pw['vio_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['vio_color'].value + sq

                    if pw['vio_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['vio_f_row'].value + sq

                    if pw['vio_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['vio_f_col'].value + sq


                    if pw['vio_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['vio_n_hov'].value + sq

                    if pw['vio_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['vio_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)




                    if pw['vio_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['vio_x_min'].value), int(pw['vio_x_max'].value)]
                    if pw['vio_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['vio_y_min'].value), int(pw['vio_y_max'].value)]


                    if pw['vio_ori'].value == None:
                        orix = None
                    else:
                        orix =  sq + pw['vio_ori'].value + sq




                    plt_st = "px.violin(df,    x = {x} ,     y = {y},  title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} ,  facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name}, orientation = {orientation},hover_data = {hover_data}, box = {boxx})".format(x = xx,    y = yx,      title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx , hover_data = d_hovx ,  range_x =rangexx , range_y = rangeyy ,      facet_row = f_rowx,   facet_col =f_colx,    hover_name =n_hovx   , orientation = orix , boxx = pw['vio_box'].value )

                    fig = eval(plt_st)

                 #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "histogram":

                    if pw['hist_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['hist_x'].value + sq

                    if pw['hist_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['hist_log_x'].value 

                    if pw['hist_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['hist_log_y'].value 




                    if pw['hist_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['hist_y'].value + sq

                    if pw['hist_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['hist_title'].value + sq

                    if pw['hist_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['hist_color'].value + sq

                    if pw['hist_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['hist_f_row'].value + sq

                    if pw['hist_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['hist_f_col'].value + sq


                    if pw['hist_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['hist_n_hov'].value + sq

                    if pw['hist_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['hist_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)


                    if pw['hist_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['hist_x_min'].value), int(pw['hist_x_max'].value)]
                    if pw['hist_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['hist_y_min'].value), int(pw['hist_y_max'].value)]


                    if pw['hist_ori'].value == None:
                        orix = None
                    else:
                        orix =  sq + pw['hist_ori'].value + sq

                    if pw['hist_nbins'].value == "":
                        nbins = None
                    else:
                        nbins =  int(pw['hist_nbins'].value )

                    if pw['hist_marg'].value == None:
                        margx = None
                    else:
                        margx =  sq +pw['hist_marg'].value + sq




                    plt_st = "px.histogram(df,    x = {x} ,     y = {y},  title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} ,  facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name},hover_data = {hover_data}, orientation = {orientation},nbins = {nbins}, marginal = {marginal})".format(x = xx,    y = yx,      title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,      range_x =rangexx , range_y = rangeyy ,   hover_data = d_hovx,   facet_row = f_rowx,   facet_col =f_colx,    hover_name =n_hovx   , orientation = orix  ,nbins =  nbins, marginal = margx)

                    fig = eval(plt_st)

                #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "strip":


                    if pw['strip_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['strip_x'].value + sq

                    if pw['strip_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['strip_log_x'].value 

                    if pw['strip_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['strip_log_y'].value 




                    if pw['strip_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['strip_y'].value + sq

                    if pw['strip_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['strip_title'].value + sq

                    if pw['strip_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['strip_color'].value + sq

                    if pw['strip_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['strip_f_row'].value + sq

                    if pw['strip_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['strip_f_col'].value + sq


                    if pw['strip_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['strip_n_hov'].value + sq

                    if pw['strip_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['strip_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)



                    if pw['strip_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['strip_x_min'].value), int(pw['strip_x_max'].value)]
                    if pw['strip_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['strip_y_min'].value), int(pw['strip_y_max'].value)]


                    if pw['strip_ori'].value == None:
                        orix = None
                    else:
                        orix =  sq + pw['strip_ori'].value + sq




                    plt_st = "px.strip(df,    x = {x} ,     y = {y},  title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} ,  facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name},hover_data = {hover_data}, orientation = {orientation})".format(x = xx,    y = yx,      title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,      range_x =rangexx , range_y = rangeyy ,      facet_row = f_rowx,   facet_col =f_colx,   hover_data = d_hovx, hover_name =n_hovx   , orientation = orix  )

                    fig = eval(plt_st)

                             #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "area":

                    if pw['area_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['area_x'].value + sq

                    if pw['area_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['area_log_x'].value 

                    if pw['area_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['area_log_y'].value 




                    if pw['area_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['area_y'].value + sq

                    if pw['area_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['area_title'].value + sq

                    if pw['area_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['area_color'].value + sq

                    if pw['area_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['area_f_row'].value + sq

                    if pw['area_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['area_f_col'].value + sq


                    if pw['area_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['area_n_hov'].value + sq


                    if pw['area_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['area_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)


                    if pw['area_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['area_x_min'].value), int(pw['area_x_max'].value)]
                    if pw['area_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['area_y_min'].value), int(pw['area_y_max'].value)]


                    if pw['area_ori'].value == None:
                        orix = None
                    else:
                        orix =  sq + pw['area_ori'].value + sq




                    plt_st = "px.area(df,    x = {x} ,     y = {y},  title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} , hover_data = {hover_data}, facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name}, orientation = {orientation})".format(x = xx,    y = yx,      title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,      range_x =rangexx , range_y = rangeyy ,      facet_row = f_rowx,   facet_col =f_colx,    hover_name =n_hovx  ,hover_data = d_hovx , orientation = orix  )

                    fig = eval(plt_st)

                #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "density_heatmap":

                    if pw['dh_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['dh_x'].value + sq

                    if pw['dh_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['dh_log_x'].value 

                    if pw['dh_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['dh_log_y'].value 

                    if pw['dh_mar_x'].value == None:
                        marxx = None
                    else:
                        marxx =  sq + pw['dh_mar_x'].value + sq

                    if pw['dh_mar_y'].value == None:
                        maryx = None
                    else:
                        maryx =  sq + pw['dh_mar_y'].value + sq


                    if pw['dh_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['dh_y'].value + sq

                    if pw['dh_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['dh_title'].value + sq

                    if pw['dh_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['dh_color'].value + sq

                    if pw['dh_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['dh_f_row'].value + sq

                    if pw['dh_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['dh_f_col'].value + sq


                    if pw['dh_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['dh_n_hov'].value + sq

                    if pw['dh_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['dh_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)




                    if pw['dh_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['dh_x_min'].value), int(pw['dh_x_max'].value)]
                    if pw['dh_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['dh_y_min'].value), int(pw['dh_y_max'].value)]


                    #print(d_hovx)

                    plt_st = "px.density_heatmap(df,    x = {x} ,     y = {y},  title = {title},   log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} ,  facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name},   marginal_x = {marginal_x},    hover_data = {hover_data},    marginal_y={marginal_y})".format(x = xx,    y = yx,      title =titlex ,          log_x =log_xx , log_y =log_yx ,      range_x =rangexx , range_y = rangeyy ,      facet_row = f_rowx,   facet_col =f_colx,    hover_name =n_hovx ,    hover_data = d_hovx,   marginal_x =marxx ,     marginal_y =maryx  )

                    fig = eval(plt_st)

                    #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "density_contour":

                    if pw['dc_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['dc_x'].value + sq

                    if pw['dc_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['dc_log_x'].value 

                    if pw['dc_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['dc_log_y'].value 

                    if pw['dc_mar_x'].value == None:
                        marxx = None
                    else:
                        marxx =  sq + pw['dc_mar_x'].value + sq

                    if pw['dc_mar_y'].value == None:
                        maryx = None
                    else:
                        maryx =  sq + pw['dc_mar_y'].value + sq


                    if pw['dc_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['dc_y'].value + sq

                    if pw['dc_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['dc_title'].value + sq

                    if pw['dc_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['dc_color'].value + sq

                    if pw['dc_f_row'].value == None:
                        f_rowx = None
                    else:
                        f_rowx =  sq + pw['dc_f_row'].value + sq

                    if pw['dc_f_col'].value == None:
                        f_colx = None
                    else:
                        f_colx =  sq + pw['dc_f_col'].value + sq


                    if pw['dc_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['dc_n_hov'].value + sq


                    if pw['dc_d_hov'].value == None:
                        d_hovx = None
                    else:
                        if pw['dc_d_hov'].value == 'All columns':
                            d_hovx =list(df.columns)

                    if pw['dc_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['dc_x_min'].value), int(pw['dc_x_max'].value)]
                    if pw['dc_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['dc_y_min'].value), int(pw['dc_y_max'].value)]


                    #print(d_hovx)
                    #
                    plt_st = "px.density_contour(df,    x = {x} ,     y = {y},  title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} ,  range_x={range_x}    ,  range_y ={range_y} ,  facet_row = {facet_row},  facet_col = {facet_col},   hover_name={hover_name},   marginal_x = {marginal_x}, hover_data =  {hover_data},       marginal_y={marginal_y})".format(x = xx,    y = yx,      title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,      range_x =rangexx , range_y = rangeyy ,      facet_row = f_rowx,   facet_col =f_colx,  hover_data =  d_hovx,  hover_name =n_hovx ,       marginal_x =marxx ,     marginal_y =maryx  )

                    fig = eval(plt_st)


                 #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "scatter_3d":


                    if pw['scatt3_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['scatt3_x'].value + sq

                    if pw['scatt3_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['scatt3_y'].value + sq

                    if pw['scatt3_z'].value == None:
                        zx = None
                    else:
                        zx =  sq + pw['scatt3_z'].value + sq

                    if pw['scatt3_title'].value =="":
                        titlex = None
                    else:
                        titlex = sq+ pw['scatt3_title'].value + sq

                    if pw['scatt3_color'].value == None:
                        colorx = None
                    else:
                        colorx = sq+ pw['scatt3_color'].value + sq

                    #################

                    if pw['scatt3_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['scatt3_log_x'].value 

                    if pw['scatt3_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['scatt3_log_y'].value 

                    if pw['scatt3_log_z'].value == None:
                        log_zx = None
                    else:
                        log_zx =   pw['scatt3_log_z'].value 



                    if pw['scatt3_symb'].value == None:
                        symbx = None
                    else:
                        symbx =  sq + pw['scatt3_symb'].value + sq

                    if pw['scatt3_size'].value == None:
                        sizex = None
                    else:
                        sizex =  sq + pw['scatt3_size'].value + sq


                    if pw['scatt3_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['scatt3_x_min'].value), int(pw['scatt3_x_max'].value)]
                    if pw['scatt3_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['scatt3_y_min'].value), int(pw['scatt3_y_max'].value)]

                    if pw['scatt3_z_min'].value == "":
                        rangezz = None
                    else:
                        rangezz = [int(pw['scatt3_z_min'].value), int(pw['scatt3_z_max'].value)]



                    plt_st = "px.scatter_3d(df,    x = {x} ,     y = {y}, z = {z}, title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} , log_z = {log_z}, range_x={range_x}    ,  range_y ={range_y} , range_z = {range_z},    size={size},      symbol = {symbol})".format(x = xx,    y = yx,   z = zx,   title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,  log_z = log_zx, range_z =  rangezz,   range_x =rangexx , range_y = rangeyy ,      size = sizex,          symbol =symbx )
                    fig =  eval(plt_st)

                     #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "line_3d":
                    if pw['line3_x'].value == None:
                        xx = None
                    else:
                        xx =  sq + pw['line3_x'].value + sq

                    if pw['line3_y'].value == None:
                        yx = None
                    else:
                        yx =  sq + pw['line3_y'].value + sq

                    if pw['line3_z'].value == None:
                        zx = None
                    else:
                        zx =  sq + pw['line3_z'].value + sq

                    if pw['line3_title'].value =="":
                        titlex = None
                    else:
                        titlex = sq+ pw['line3_title'].value + sq

                    if pw['line3_color'].value == None:
                        colorx = None
                    else:
                        colorx = sq+ pw['line3_color'].value + sq

                    #################

                    if pw['line3_log_x'].value == None:
                        log_xx = None
                    else:
                        log_xx =   pw['line3_log_x'].value 

                    if pw['line3_log_y'].value == None:
                        log_yx = None
                    else:
                        log_yx =   pw['line3_log_y'].value 

                    if pw['line3_log_z'].value == None:
                        log_zx = None
                    else:
                        log_zx =   pw['line3_log_z'].value 



                    if pw['line3_symb'].value == None:
                        symbx = None
                    else:
                        symbx =  sq + pw['line3_symb'].value + sq

                    if pw['line3_ld'].value == None:
                        line_dashx = None
                    else:
                        line_dashx =  sq + pw['line3_ld'].value + sq

                    if pw['line3_size'].value == None:
                        sizex = None
                    else:
                        sizex =  sq + pw['line3_size'].value + sq




                    if pw['line3_x_min'].value == "":
                        rangexx = None
                    else:
                        rangexx = [int(pw['line3_x_min'].value), int(pw['line3_x_max'].value)]
                    if pw['line3_y_min'].value == "":
                        rangeyy = None
                    else:
                        rangeyy = [int(pw['line3_y_min'].value), int(pw['line3_y_max'].value)]

                    if pw['line3_z_min'].value == "":
                        rangezz = None
                    else:
                        rangezz = [int(pw['line3_z_min'].value), int(pw['line3_z_max'].value)]



                    plt_st = "px.line_3d(df,    x = {x} ,     y = {y}, z = {z}, title = {title}, color = {color},  log_x  ={log_x}   ,log_y = {log_y} , log_z = {log_z}, range_x={range_x}    ,  range_y ={range_y} , range_z = {range_z}, line_dash = {line_dash})".format(x = xx,    y = yx,   z = zx,   title =titlex ,       color =colorx,      log_x =log_xx , log_y =log_yx ,  log_z = log_zx, range_z =  rangezz,   range_x =rangexx , range_y = rangeyy ,line_dash = line_dashx )
                    #print(plt_st)
                    fig =  eval(plt_st)


                #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "scatter_matrix":   
                    if pw['scatt_m_sym'].value == None:
                        symbx = None
                    else:
                        symbx =  sq + pw['scatt_m_sym'].value + sq

                    if pw['scatt_m_size'].value == None:
                        sizex = None
                    else:
                        sizex =  sq + pw['scatt_m_size'].value + sq


                    if pw['scatt_m_title'].value == "":
                        titlex = None
                    else:
                        titlex =  sq + pw['scatt_m_title'].value + sq

                    if pw['scatt_m_color'].value == None:
                        colorx = None
                    else:
                        colorx =  sq + pw['scatt_m_color'].value + sq



                    if pw['scatt_m_n_hov'].value == None:
                        n_hovx = None
                    else:
                        n_hovx =  sq + pw['scatt_m_n_hov'].value + sq

                    if pw['scatt_m_d_hov'].value == None:
                        d_hovx = None
                    else:
                        d_hovx = list(df.columns)



                    plt_st = "px.scatter_matrix(df,  title = {title}, color = {color}, size = {size},symbol = {symbol},hover_name={hover_name}, hover_data = {hover_data})".format(   title =titlex , hover_data =  d_hovx,  color =colorx  , size = sizex , symbol  = symbx, hover_name = n_hovx)

                    fig =  eval(plt_st)



                #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "parallel_coordinates": 

                    if pw['p_coor_title'].value =="":
                        titlex = None
                    else:
                        titlex = sq+ pw['p_coor_title'].value + sq

                    if pw['p_coor_color'].value == None:
                        colorx = None
                    else:
                        colorx = sq+ pw['p_coor_color'].value + sq





                    plt_st = "px.parallel_coordinates(df,  title = {title}, color = {color})".format(   title =titlex ,       color =colorx   )
                    #print(plt_st)
                    fig =  eval(plt_st)


                 #'scatter','box','violin','histogram','strip','density_heatmap','density_contour','area','scatter_3d','line_3d','scatter_matrix','parallel_coordinates','parallel_categories'

                if plt_dig.value == "parallel_categories":

                    if pw['p_cat_title'].value =="":
                        titlex = None
                    else:
                        titlex = sq+ pw['p_cat_title'].value + sq

                    if pw['p_cat_color'].value == None:
                        colorx = None
                    else:
                        colorx = sq+ pw['p_cat_color'].value + sq



                    p_cat_h2 =  widgets.HBox([pw['p_cat_dim']])

                    plt_st = "px.parallel_categories(df,  title = {title}, color = {color})".format(   title =titlex ,       color =colorx   )
                    #print(plt_st)
                    fig =  eval(plt_st)



                ###########################################################################################################
                #plt_dig.value = None
                display(plt_head)
                display(plt_slt)
                display(bplt)
                display(lineout)
                plt_st = plt_st.replace(' ','')
                display(plt_st)
                display(lineout)
                fig.show()
            ###########################################################################################################

            #############################################################################################
            display(lineout)
            display(bplt)
            bplt.on_click(functools.partial(on_bplt_clicked))
            #bsplt.on_click(functools.partial(plt_response))
            ######################################################################################################

        def plt_responsex(cntrl):

                clear_output()
                display(plt_head)
                display(plt_slt)
                display(bplt)
                #widgs()


        def pltupd_response(cntrl):
            plt_responsex('upd')
            #clear_output()
            #widgs()



        def plthlp_response(cntrl):
            clear_output()
            display(plt_head)

            display('~ x         : Set column to be displayed on x-Axis')
            display('~ y         : Set column to be displayed on y-Axis')
            display('~ title     : Set plot title')
            display('~ color     : Add colors to plot based on values of a column')
            display('~ x_min     : Set min values of the x-axis(y_min, z_min)' )
            display('~ x_max     : set max values of the x-axis(y-max,z_max)')
            display('~ f_row     : Create veritcal subplots based on column values')
            display('~ f_col     : Create horizontal subplots based on column values')
            display('~ n_hov     : Column value which will appear as a title in hover box')
            display('~ d_hov     : Column value which will appear in hover info')
            display('~ log_x     : Transform x-axis to show logarithim of vlaues(log_y,log_z)')
            display('~ size      : Add different size points to plot based on values of a column')
            
            display('~ symb      : Add different symbols to plot based on values of a column')
            display('~ ld        : Add different line dashes to plot based on values of a column')
            display('~ mar_x     : Add a marginal distribution of x values ( y vales, z values)')
            display('~ s_max     : Set size of the point in the plot')
            patho = eval('pd.__file__')
            patho =  patho.replace('pandas\__init__.py','')
            file = open(patho + 'pandas_ui\zis.jpg', 'rb')
            image = file.read()
            display(lineout)
            display('                                                             Reference                                                               ')
            display(lineout)
            f_w = widgets.Image(
                value=image,
                format='jpg',
                width=1000,
                height=700,
                )
            display(f_w)


        ######################################################################################################




        plt_dig.observe(plt_responsex, names = "value")


        bplt = widgets.Button(description='Plot')
        bplt.style.button_color = 'green'

        bsplt = widgets.Button(description='Choose')
        #bsplt.style.button_color = 'gray'

        plt_slt =  widgets.HBox([plt_dig, bsplt])
        bsplt.on_click(functools.partial(plt_response))


        label_layout3p = Layout(width='125px', height='30px')

        label_layout5p = Layout(width='150px', height='30px')

        bhplt_layout = Layout(width='250px', height='35px', border='2px solid white')
        pltupd =  widgets.Button(description= 'View/Update',button_style = 'Success', icon = 'fa-cubes')
        head_pltlabel = widgets.Button(description= 'Plot', button_style = 'Success')
        plthlp = widgets.Button(description= 'help', button_style = 'Success', icon = 'fa-question-circle' )
        lineout = widgets.Output(layout={'border': '1px solid black'})
        pltheadl = HBox([
                        pltupd,
                        Label('', layout=label_layout5p),
                        Label('', layout=label_layout5p), Label('Plot'),
                        Label('', layout=label_layout3p),

                        Label('', layout=label_layout5p), plthlp
                    ])


        pltupd.on_click(functools.partial(pltupd_response))
        plthlp.on_click(functools.partial(plthlp_response))

        plt_head =  widgets.VBox([lineout,pltheadl,lineout])

        display(plt_head)
        display(plt_slt)
        display(bplt)




        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        
    children = [tab_c1, tab_c2, tab_c3, tab_c4]

    tab.children = children
    for i, j in zip((0, 1, 2, 3), ["DataFrame", "PandasProfoling", "Explore", "Commands"]):
        tab.set_title(i, j)

    #display(icon)
    display(tab)

    
    # Deal with ba    ck button by interchanging the bcb and bb/ have look into it.
    
    
def pandas_ui(path):
    try:
        pandas_ui1(path)
    except:
        
        js = '<script>alert("Exception arised");</script>'
        display(HTML(js))
        raise
        #print('.....')
        ###display(HTML(js))
        
        
def get_df():
    return student.dataf
def get_pivotdf():
    return student.pivotdf
def get_meltdf():
    return student.meltdf

if __name__ == "__main__":
	main()
