
# modules_downloaded_from: "http://selenium-release.storage.googleapis.com/index.html?path=3.150/"
#file_structure:
#  *  IEDriverServer_Win32_.3.150.2
#    * IEDriverServer.exe
#  *  IEDriverServer_Win32_3.150.1
#    * IEDriverServer.exe
#  *  IEDriverServer_Win32_.3.150.2.zip
#  *  IEDriverServer_Win32_3.150.1.zip



import psutil, sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.ie.options import Options as IE_Options
from webdriver_manager.microsoft import IEDriverManager

def kill_process(kill_targets ):
    while True:
        for proc in psutil.process_iter():
            #break
            if proc.name() in kill_targets:
                try:
                    proc.kill()
                except:
                    print("proc.kill() failed")
        pname_list = [x.name() for x in psutil.process_iter()]
        for x in kill_targets:
            if x in pname_list:
                print(f"process:{x} killing failed.")
                continue
        break

wd, dm = webdriver.Ie, IEDriverManager
kill_targets = ["iexplore.exe"]


try_phase = "by-downloaded-exe-file-(32bit-old-version, 3.150.1)" ; print(f"try_phase:{try_phase}")
try:
    kill_process(["iexplore.exe"])
    options = IE_Options()
    ex_path_win32 = "IEDriverServer_Win32_3.150.1/IEDriverServer.exe"
    driver = wd(options=options, executable_path = ex_path_win32)
    driver.get("https://www.google.com")
    res = driver.find_element_by_xpath("/html")
    print(f"\t find_element_by_xpath, result:{res}")
    raise ValueError("normally-executed")
except Exception as ex:
    print(f"\t exception-content:{ex}")
print()


try_phase = "by-downloaded-exe-file-(32bit)" ; print(f"try_phase:{try_phase}")
try:
    kill_process(["iexplore.exe"])
    options = IE_Options()
    ex_path_win32 = "IEDriverServer_Win32_.3.150.2/IEDriverServer.exe"
    driver = wd(options=options, executable_path = ex_path_win32)
    driver.get("https://www.google.com")
    res = driver.find_element_by_xpath("/html")
    print(f"\t find_element_by_xpath, result:{res}")
except Exception as ex:
    print(f"\t exception-content:{ex}")
print()

try_phase = "by-IEDriverManager-distribution"
try:
    kill_process(["iexplore.exe"])
    options = IE_Options()
    driver = wd(options=options, executable_path=dm().install())
    driver.get("https://www.google.com")
    res = driver.find_element_by_xpath("/html")
    print(f"\t find_element_by_xpath, result:{res}")
    raise ValueError("normally-executed")
except Exception as ex:
    print(f"\t exception-content:{ex}")
print()

