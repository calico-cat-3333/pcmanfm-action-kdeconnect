#!/usr/bin/env python3
import os
import sys
import locale
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#created by glade
ui_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.40.0 -->
<interface>
  <requires lib="gtk+" version="3.24"/>
  <object class="GtkWindow" id="window">
    <property name="can-focus">False</property>
    <property name="title" translatable="yes">Send To</property>
    <property name="default-width">300</property>
    <property name="icon-name">phone</property>
    <child>
      <!-- n-columns=2 n-rows=5 -->
      <object class="GtkGrid" id="win_grid">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <child>
          <object class="GtkScrolledWindow">
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">7</property>
            <property name="margin-end">7</property>
            <property name="hexpand">True</property>
            <property name="vexpand">True</property>
            <property name="shadow-type">in</property>
            <property name="min-content-height">100</property>
            <child>
              <object class="GtkViewport">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <child>
                  <object class="GtkListBox" id="files_list">
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">1</property>
            <property name="width">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkScrolledWindow">
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="margin-start">7</property>
            <property name="margin-end">7</property>
            <property name="hexpand">True</property>
            <property name="vexpand">True</property>
            <property name="shadow-type">in</property>
            <property name="min-content-height">100</property>
            <child>
              <object class="GtkViewport">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <child>
                  <object class="GtkListBox" id="devices_list">
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">3</property>
            <property name="width">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="files_label">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-start">7</property>
            <property name="margin-top">7</property>
            <property name="margin-bottom">3</property>
            <property name="label" translatable="yes">Send following Files:</property>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">0</property>
            <property name="width">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="devices_label">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="halign">start</property>
            <property name="margin-start">7</property>
            <property name="margin-top">7</property>
            <property name="margin-bottom">3</property>
            <property name="hexpand">False</property>
            <property name="label" translatable="yes">To Devices:</property>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">2</property>
            <property name="width">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="cancel_button">
            <property name="label">gtk-cancel</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <property name="halign">end</property>
            <property name="margin-top">7</property>
            <property name="margin-bottom">7</property>
            <property name="hexpand">True</property>
            <property name="use-stock">True</property>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">4</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="ok_button">
            <property name="label">gtk-ok</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <property name="halign">end</property>
            <property name="margin-start">5</property>
            <property name="margin-end">7</property>
            <property name="margin-top">7</property>
            <property name="margin-bottom">7</property>
            <property name="use-stock">True</property>
          </object>
          <packing>
            <property name="left-attach">1</property>
            <property name="top-attach">4</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
'''
trans = {
    'en':{ #translated with deepl and microsoft trasnlation
        'Error':'Error',
        'No file selected.':'No file selected.',
        ' is not a file.':' is not a file.',
        'No connected device.':'No connected device.',
        'No receiving device selected.':'No receiving device selected.',
        'Program error, process exit ':'Program error, process exit ',
        'Send via KDE Connect':'Send via KDE Connect',
        'Send the following files:':'Send the following files:',
        'To the device:':'To the device'
        },
    'zh':{
        'Error':'错误',
        'No file selected.':'未选择文件',
        ' is not a file.':' 不是一个文件',
        'No connected device.':'无已连接的设备',
        'No receiving device selected.':'未选择接收设备',
        'Program error, process exit ':'程序错误，进程退出',
        'Send via KDE Connect':'发送到设备',
        'Send the following files:':'发送下列文件：',
        'To the device:':'到设备：'
        }
    }

def getlang():
    if locale.getlocale(category=locale.LC_CTYPE) == ('zh_CN', 'UTF-8'):
        lang = 'zh'
    else:
        lang = 'en'
    return lang

display_string = trans[getlang()]

def create_files_listboxrow():
    for fileitem in filelist:
        listitem = Gtk.ListBoxRow()
        listitem.add(Gtk.Label(label=fileitem, halign=Gtk.Align.START))
        files_list_box.add(listitem)

def get_devices_list():
    dl = []
    with os.popen('kdeconnect-cli --list-available --id-name-only') as rt:
        for li in rt:
            sli = li.strip()
            dev = sli.split(' ', 1)
            dl.append(dev)
    return dl

class devicelbrow(Gtk.ListBoxRow):
    def __init__(self, label='label', devid=''):
        super().__init__()
        self.checkbutton = Gtk.CheckButton(label=label)
        self.checkbutton.connect('toggled', self.on_toggled)
        self.device_id = devid
        self.add(self.checkbutton)
    def on_toggled(self,widget):
        if self.checkbutton.get_active():
            selected_devicelist.append(self.device_id)
        else:
            selected_devicelist.remove(self.device_id)

def create_devices_listboxrow():
    for deviceitem in devicelist:
        listitem = devicelbrow(label=deviceitem[1], devid=deviceitem[0])
        devices_list_box.add(listitem)

def show_help():
    print('Useage: sendtokdeconnect.py [-h] filename ...')
    print('\t-h --help: show this help')

def process_args():
    fl = []
    for arg in args[1:]: # args[0] is self path
        if arg == '-h' or arg == '--help' :
            show_help()
            exit(0)
        fl.append(arg)
    return fl

def errordialog(message = ''):
    dialog = Gtk.MessageDialog(transient_for=win,
                               flags=0,
                                message_type=Gtk.MessageType.ERROR,
                                buttons=Gtk.ButtonsType.CANCEL,
                                text=display_string['Error'],)
    dialog.format_secondary_text(message)
    dialog.run()
    dialog.destroy()

def checkfilelsit():
    if len(filelist) == 0:
        print(display_string['Error']+': '+display_string['No file selected.'])
        errordialog(display_string['No file selected.'])
        exit(0)
    for item in filelist:
        if not os.path.isfile(item):
            print(display_string['Error']+': '+item+display_string['No file selected.'][' is not a file.'])
            errordialog(item+display_string[' is not a file.'])
            exit(1)

def checkdevicelist():
    if len(devicelist) == 0:
        print(display_string['Error']+': '+display_string['No connected device.'])
        errordialog(display_string['No connected device.'])
        exit(1)

def send(widget):
    if len(selected_devicelist) == 0:
        print(display_string['Error']+': '+display_string['No receiving device selected.'])
        errordialog(display_string['No receiving device selected.'])
        return
    #print('send ',filelist,' to ',selected_devicelist)
    filestr = ''
    for fileitem in filelist:
        filestr = filestr + ' "' + fileitem + '"'
    _cmd = 'kdeconnect-cli --device '
    for device in selected_devicelist:
        cmd = _cmd + device + ' --share' + filestr
        r = os.system(cmd)
        if (r >> 8) != 0:
            print(display_string['Error']+': '+display_string['Program error, process exit ']+str(r))
            errordialog(display_string['Program error, process exit ']+str(r))
            break
    Gtk.main_quit()

if __name__ == '__main__':
    builder = Gtk.Builder()
    builder.add_from_string(ui_xml)
    win = builder.get_object('window')
    win.connect('delete-event', Gtk.main_quit)
    win.set_title(display_string['Send via KDE Connect'])

    builder.get_object('files_label').set_label(display_string['Send the following files:'])
    builder.get_object('devices_label').set_label(display_string['To the device:'])

    args = sys.argv
    filelist = process_args()
    checkfilelsit()
    devicelist = get_devices_list()
    checkdevicelist()
    selected_devicelist = []

    files_list_box = builder.get_object('files_list')
    create_files_listboxrow()

    #print(devicelist)
    devices_list_box = builder.get_object('devices_list')
    create_devices_listboxrow()

    cancel_button = builder.get_object('cancel_button')
    cancel_button.connect('clicked', Gtk.main_quit)
    ok_button = builder.get_object('ok_button')
    ok_button.connect('clicked', send)

    win.show_all()
    Gtk.main()
