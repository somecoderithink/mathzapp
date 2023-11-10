#######################################################################################################################
# MATHZAPP
# just a simple python script which helps studentz
#######################################################################################################################
# GitHub Repository
# https://github.com/somecoderithink/mathzapp
#######################################################################################################################
# My Website
# https://aadityas.rf.gd/
#######################################################################################################################
# THIS SOFTWARE IS LICENSED UNDER THE MIT LICENSE
#
# Copyright 2023 aadityas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#######################################################################################################################
import statistics
import sys
import os
import urllib.request
import time
import math
from rich.progress import track
from colorama import Fore, Style

def osinfo():
    if os.name == "linux":
        print(Fore.YELLOW + "You are running this program on Linux." + Style.RESET_ALL)
        print()
    elif os.name == "darwin":
        print(Fore.YELLOW + "You are running this program on Mac." + Style.RESET_ALL)
        print()
    elif os.name == "nt":
        print(Fore.YELLOW + "You are running this program on Windows." + Style.RESET_ALL)
        print()
    else:
        print(Fore.YELLOW + "You are running this program on Android." + Style.RESET_ALL)

def clr_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_header():
    print(Fore.RED + "  __  __       _   _                  _____  _____  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  \/  |     | | | |           /\   |  __ \|  __ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | \  / | __ _| |_| |__  ____  /  \  | |__) | |__) |" + Style.RESET_ALL)
    print(Fore.BLUE + " | |\/| |/ _` | __| '_ \|_  / / /\ \ |  ___/|  ___/ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  | | (_| | |_| | | |/ / / ____ \| |    | |     " + Style.RESET_ALL)
    print(Fore.CYAN + " |_|  |_|\__,_|\__|_| |_/___/_/    \_\_|    |_|     " + Style.RESET_ALL)
    print("------------ created by Aaditya Sharma -------------")
    print()

def addition_header():
    print(Fore.RED + "              _     _ _ _   _             " + Style.RESET_ALL)
    print(Fore.GREEN + "     /\      | |   | (_) | (_)            " + Style.RESET_ALL)
    print(Fore.YELLOW + "    /  \   __| | __| |_| |_ _  ___  _ __  " + Style.RESET_ALL)
    print(Fore.BLUE + "   / /\ \ / _` |/ _` | | __| |/ _ \| '_ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + "  / ____ \ (_| | (_| | | |_| | (_) | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " /_/    \_\__,_|\__,_|_|\__|_|\___/|_| |_|" + Style.RESET_ALL)
    print("------------------------------------------")
    print()

def subtraction_header():
    print(Fore.RED + "   _____       _     _                  _   _             " + Style.RESET_ALL)
    print(Fore.GREEN + "  / ____|     | |   | |                | | (_)            " + Style.RESET_ALL)
    print(Fore.YELLOW + " | (___  _   _| |__ | |_ _ __ __ _  ___| |_ _  ___  _ __  " + Style.RESET_ALL)
    print(Fore.BLUE + "  \___ \| | | | '_ \| __| '__/ _` |/ __| __| |/ _ \| '_ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + "  ____) | |_| | |_) | |_| | | (_| | (__| |_| | (_) | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_____/ \__,_|_.__/ \__|_|  \__,_|\___|\__|_|\___/|_| |_|" + Style.RESET_ALL)
    print("----------------------------------------------------------")
    print()

def multiplication_header():
    print(Fore.RED + "  __  __       _ _   _       _ _           _   _             " + Style.RESET_ALL)
    print(Fore.GREEN + " |  \/  |     | | | (_)     | (_)         | | (_)            " + Style.RESET_ALL)
    print(Fore.YELLOW + " | \  / |_   _| | |_ _ _ __ | |_  ___ __ _| |_ _  ___  _ __  " + Style.RESET_ALL)
    print(Fore.BLUE + " | |\/| | | | | | __| | '_ \| | |/ __/ _` | __| |/ _ \| '_ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  | | |_| | | |_| | |_) | | | (_| (_| | |_| | (_) | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|  |_|\__,_|_|\__|_| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|" + Style.RESET_ALL)
    print(Fore.RED + "                      | |                                    " + Style.RESET_ALL)
    print(Fore.GREEN + "                      |_|                                    " + Style.RESET_ALL)
    print("-------------------------------------------------------------")
    print()

def division_header():
    print(Fore.RED + "  _____  _       _     _             " + Style.RESET_ALL)
    print(Fore.GREEN + " |  __ \(_)     (_)   (_)            " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |  | |___   ___ ___ _  ___  _ __  " + Style.RESET_ALL)
    print(Fore.BLUE + " | |  | | \ \ / / / __| |/ _ \| '_ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |__| | |\ V /| \__ \ | (_) | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_____/|_| \_/ |_|___/_|\___/|_| |_|" + Style.RESET_ALL)
    print("------------------------------------")
    print()

def average_header():
    print(Fore.RED + "                                        " + Style.RESET_ALL)
    print(Fore.GREEN + "     /\                                 " + Style.RESET_ALL)
    print(Fore.YELLOW + "    /  \__   _____ _ __ __ _  __ _  ___ " + Style.RESET_ALL)
    print(Fore.BLUE + "   / /\ \ \ / / _ \ '__/ _` |/ _` |/ _ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + "  / ____ \ V /  __/ | | (_| | (_| |  __/" + Style.RESET_ALL)
    print(Fore.CYAN + " /_/    \_\_/ \___|_|  \__,_|\__, |\___|" + Style.RESET_ALL)
    print(Fore.RED + "                              __/ |     " + Style.RESET_ALL)
    print(Fore.GREEN + "                             |___/      " + Style.RESET_ALL)
    print("-----------------------------------------")
    print()

def mode_header():
    print(Fore.RED + "  __  __           _      " + Style.RESET_ALL)
    print(Fore.GREEN + " |  \/  |         | |     " + Style.RESET_ALL)
    print(Fore.YELLOW + " | \  / | ___   __| | ___ " + Style.RESET_ALL)
    print(Fore.BLUE + " | |\/| |/ _ \ / _` |/ _ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  | | (_) | (_| |  __/" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|  |_|\___/ \__,_|\___|" + Style.RESET_ALL)
    print("----------------------------")
    print()

def mean_header():
    print(Fore.RED + "  __  __                  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  \/  |                 " + Style.RESET_ALL)
    print(Fore.YELLOW + " | \  / | ___  __ _ _ __  " + Style.RESET_ALL)
    print(Fore.BLUE + " | |\/| |/ _ \/ _` | '_ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  | |  __/ (_| | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|  |_|\___|\__,_|_| |_|" + Style.RESET_ALL)
    print("--------------------------")
    print()

def median_header():
    print(Fore.RED + "  __  __          _ _             " + Style.RESET_ALL)
    print(Fore.GREEN + " |  \/  |        | (_)            " + Style.RESET_ALL)
    print(Fore.YELLOW + " | \  / | ___  __| |_  __ _ _ __  " + Style.RESET_ALL)
    print(Fore.BLUE + " | |\/| |/ _ \/ _` | |/ _` | '_ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  | |  __/ (_| | | (_| | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|  |_|\___|\__,_|_|\__,_|_| |_|" + Style.RESET_ALL)
    print("----------------------------------")
    print()

def m_speed_header():
    print(Fore.RED + "   _____                     _    ___                       ____  " + Style.RESET_ALL)
    print(Fore.GREEN + "  / ____|                   | |  / (_)                     / /\ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | (___  _ __   ___  ___  __| | | | _ _ __    _ __ ___    / /__| |" + Style.RESET_ALL)
    print(Fore.BLUE + "  \___ \| '_ \ / _ \/ _ \/ _` | | || | '_ \  | '_ ` _ \  / / __| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + "  ____) | |_) |  __/  __/ (_| | | || | | | | | | | | | |/ /\__ \ |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_____/| .__/ \___|\___|\__,_| | ||_|_| |_| |_| |_| |_/_/ |___/ |" + Style.RESET_ALL)
    print(Fore.RED + "        | |                      \_\                          /_/ " + Style.RESET_ALL)
    print(Fore.GREEN + "        |_|                                                       " + Style.RESET_ALL)
    print("--------------------------------------------------------------------------")
    print()

def km_speed_header():
    print(Fore.RED + "  _____                     _    ___         _                  ___   __  " + Style.RESET_ALL)
    print(Fore.GREEN + " / ____|                   | |  / (_)       | |                / / |  \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + "| (___  _ __   ___  ___  __| | | | _ _ __   | | ___ __ ___    / /| |__ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " \___ \| '_ \ / _ \/ _ \/ _` | | || | '_ \  | |/ / '_ ` _ \  / / | '_ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " ____) | |_) |  __/  __/ (_| | | || | | | | |   <| | | | | |/ /  | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + "|_____/| .__/ \___|\___|\__,_| | ||_|_| |_| |_|\_\_| |_| |_/_/   |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "       | |                      \_\                                   /_/ " + Style.RESET_ALL)
    print(Fore.GREEN + "       |_|                                                                " + Style.RESET_ALL)
    print("--------------------------------------------------------------------------")
    print()

def speed_km_to_m_header():
    print(Fore.RED + "  _                  ___       _                        __  " + Style.RESET_ALL)
    print(Fore.GREEN + " | |                / / |     | |                      / /  " + Style.RESET_ALL)
    print(Fore.YELLOW + " | | ___ __ ___    / /| |__   | |_ ___    _ __ ___    / /__ " + Style.RESET_ALL)
    print(Fore.BLUE + " | |/ / '_ ` _ \  / / | '_ \  | __/ _ \  | '_ ` _ \  / / __|" + Style.RESET_ALL)
    print(Fore.MAGENTA + " |   <| | | | | |/ /  | | | | | || (_) | | | | | | |/ /\__ \ " + Style.RESET_ALL)
    print(Fore.CYAN + " |_|\_\_| |_| |_/_/   |_| |_|  \__\___/  |_| |_| |_/_/ |___/" + Style.RESET_ALL)
    print("------------------------------------------------------------")
    print()

def speed_m_to_km_header():
    print(Fore.RED + "                __    _          _                  ___     " + Style.RESET_ALL)
    print(Fore.GREEN + "               / /   | |        | |                / / |    " + Style.RESET_ALL)
    print(Fore.YELLOW + "  _ __ ___    / /__  | |_ ___   | | ___ __ ___    / /| |__  " + Style.RESET_ALL)
    print(Fore.BLUE + " | '_ ` _ \  / / __| | __/ _ \  | |/ / '_ ` _ \  / / | '_ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | | | | | |/ /\__ \ | || (_) | |   <| | | | | |/ /  | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_| |_| |_/_/ |___/  \__\___/  |_|\_\_| |_| |_/_/   |_| |_|" + Style.RESET_ALL)
    print("------------------------------------------------------------")
    print()

def distance_km_header():
    print(Fore.RED + "  _____  _     _                          ___            __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  __ \(_)   | |                        / / |           \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |  | |_ ___| |_ __ _ _ __   ___ ___  | || | ___ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " | |  | | / __| __/ _` | '_ \ / __/ _ \ | || |/ / '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |__| | \__ \ || (_| | | | | (_|  __/ | ||   <| | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_____/|_|___/\__\__,_|_| |_|\___\___| | ||_|\_\_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "                                         \_\             /_/ " + Style.RESET_ALL)
    print("-------------------------------------------------------------")
    print()

def distance_m_header():
    print(Fore.RED + "  _____  _     _                          __       __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  __ \(_)   | |                        / /       \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |  | |_ ___| |_ __ _ _ __   ___ ___  | |_ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " | |  | | / __| __/ _` | '_ \ / __/ _ \ | | '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |__| | \__ \ || (_| | | | | (_|  __/ | | | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_____/|_|___/\__\__,_|_| |_|\___\___| | |_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "                                         \_\       /_/ " + Style.RESET_ALL)
    print("-------------------------------------------------------")
    print()

def time_hrs_header():
    print(Fore.RED + "  _______ _                   ___            __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |__   __(_)                 / / |           \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + "    | |   _ _ __ ___   ___  | || |__  _ __ ___| |" + Style.RESET_ALL)
    print(Fore.BLUE + "    | |  | | '_ ` _ \ / _ \ | || '_ \| '__/ __| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + "    | |  | | | | | | |  __/ | || | | | |  \__ \ |" + Style.RESET_ALL)
    print(Fore.CYAN + "    |_|  |_|_| |_| |_|\___| | ||_| |_|_|  |___/ |" + Style.RESET_ALL)
    print(Fore.RED + "                             \_\             /_/ " + Style.RESET_ALL)
    print("-------------------------------------------------")
    print()

def time_sec_header():
    print(Fore.RED + "  _______ _                   __           __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |__   __(_)                 / /           \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + "    | |   _ _ __ ___   ___  | |___  ___  ___| |" + Style.RESET_ALL)
    print(Fore.BLUE + "    | |  | | '_ ` _ \ / _ \ | / __|/ _ \/ __| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + "    | |  | | | | | | |  __/ | \__ \  __/ (__| |" + Style.RESET_ALL)
    print(Fore.CYAN + "    |_|  |_|_| |_| |_|\___| | |___/\___|\___| |" + Style.RESET_ALL)
    print(Fore.RED + "                             \_\           /_/ " + Style.RESET_ALL)
    print("-----------------------------------------------")
    print()

def km_to_m_header():
    print(Fore.RED + "  _                _                    " + Style.RESET_ALL)
    print(Fore.GREEN + " | |              | |                   " + Style.RESET_ALL)
    print(Fore.YELLOW + " | | ___ __ ___   | |_ ___    _ __ ___  " + Style.RESET_ALL)
    print(Fore.BLUE + " | |/ / '_ ` _ \  | __/ _ \  | '_ ` _ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " |   <| | | | | | | || (_) | | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|\_\_| |_| |_|  \__\___/  |_| |_| |_|" + Style.RESET_ALL)
    print("----------------------------------------")
    print()

def m_to_km_header():
    print(Fore.RED + "              _          _              " + Style.RESET_ALL)
    print(Fore.GREEN + "             | |        | |             " + Style.RESET_ALL)
    print(Fore.YELLOW + "  _ __ ___   | |_ ___   | | ___ __ ___  " + Style.RESET_ALL)
    print(Fore.BLUE + " | '_ ` _ \  | __/ _ \  | |/ / '_ ` _ \ " + Style.RESET_ALL)
    print(Fore.MAGENTA + " | | | | | | | || (_) | |   <| | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_| |_| |_|  \__\___/  |_|\_\_| |_| |_|" + Style.RESET_ALL)
    print("----------------------------------------")
    print()

def hrs_to_sec_header():
    print(Fore.RED + "  _                _                        " + Style.RESET_ALL)
    print(Fore.GREEN + " | |              | |                       " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |__  _ __ ___  | |_ ___    ___  ___  ___ " + Style.RESET_ALL)
    print(Fore.BLUE + " | '_ \| '__/ __| | __/ _ \  / __|/ _ \/ __|" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | | | | |  \__ \ | || (_) | \__ \  __/ (__ " + Style.RESET_ALL)
    print(Fore.CYAN + " |_| |_|_|  |___/  \__\___/  |___/\___|\___|" + Style.RESET_ALL)
    print("--------------------------------------------")
    print()

def sec_to_hrs_header():
    print(Fore.RED + "                  _          _              " + Style.RESET_ALL)
    print(Fore.GREEN + "                 | |        | |             " + Style.RESET_ALL)
    print(Fore.YELLOW + "  ___  ___  ___  | |_ ___   | |__  _ __ ___ " + Style.RESET_ALL)
    print(Fore.BLUE + " / __|/ _ \/ __| | __/ _ \  | '_ \| '__/ __|" + Style.RESET_ALL)
    print(Fore.MAGENTA + " \__ \  __/ (__  | || (_) | | | | | |  \__ \ " + Style.RESET_ALL)
    print(Fore.CYAN + " |___/\___|\___|  \__\___/  |_| |_|_|  |___/" + Style.RESET_ALL)
    print("--------------------------------------------")
    print()

def hypotenuse_m_header():
    print(Fore.RED + "  _    _                   _                               __       __  " + Style.RESET_ALL)
    print(Fore.GREEN + " | |  | |                 | |                             / /       \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |__| |_   _ _ __   ___ | |_ ___ _ __  _   _ ___  ___  | |_ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " |  __  | | | | '_ \ / _ \| __/ _ \ '_ \| | | / __|/ _ \ | | '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  | | |_| | |_) | (_) | ||  __/ | | | |_| \__ \  __/ | | | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|  |_|\__, | .__/ \___/ \__\___|_| |_|\__,_|___/\___| | |_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "          __/ | |                                         \_\       /_/ " + Style.RESET_ALL)
    print(Fore.GREEN + "         |___/|_|                                                       " + Style.RESET_ALL)
    print("-----------------------------------------------------------------------")
    print()

def base_m_header():
    print(Fore.RED + "  ____                    __       __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  _ \                  / /       \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |_) | __ _ ___  ___  | |_ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " |  _ < / _` / __|/ _ \ | | '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |_) | (_| \__ \  __/ | | | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |____/ \__,_|___/\___| | |_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "                         \_\       /_/ " + Style.RESET_ALL)
    print("---------------------------------------")
    print()

def perpendicular_m_header():
    print(Fore.RED + "  _____                               _ _            _               __       __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  __ \                             | (_)          | |             / /       \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |__) |__ _ __ _ __   ___ _ __   __| |_  ___ _   _| | __ _ _ __  | |_ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " |  ___/ _ \ '__| '_ \ / _ \ '_ \ / _` | |/ __| | | | |/ _` | '__| | | '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  |  __/ |  | |_) |  __/ | | | (_| | | (__| |_| | | (_| | |    | | | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|   \___|_|  | .__/ \___|_| |_|\__,_|_|\___|\__,_|_|\__,_|_|    | |_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "                | |                                                 \_\       /_/ " + Style.RESET_ALL)
    print(Fore.GREEN + "                |_|                                                               " + Style.RESET_ALL)
    print("----------------------------------------------------------------------------------")
    print()

def hypotenuse_cm_header():
    print(Fore.RED + "  _    _                   _                               __            __  " + Style.RESET_ALL)
    print(Fore.GREEN + " | |  | |                 | |                             / /            \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |__| |_   _ _ __   ___ | |_ ___ _ __  _   _ ___  ___  | | ___ _ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " |  __  | | | | '_ \ / _ \| __/ _ \ '_ \| | | / __|/ _ \ | |/ __| '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  | | |_| | |_) | (_) | ||  __/ | | | |_| \__ \  __/ | | (__| | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|  |_|\__, | .__/ \___/ \__\___|_| |_|\__,_|___/\___| | |\___|_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "          __/ | |                                         \_\            /_/ " + Style.RESET_ALL)
    print(Fore.GREEN + "         |___/|_|                                                            " + Style.RESET_ALL)
    print("-----------------------------------------------------------------------------")
    print()

def base_cm_header():
    print(Fore.RED + "  ____                    __            __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  _ \                  / /            \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |_) | __ _ ___  ___  | | ___ _ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " |  _ < / _` / __|/ _ \ | |/ __| '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |_) | (_| \__ \  __/ | | (__| | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |____/ \__,_|___/\___| | |\___|_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "                         \_\            /_/ " + Style.RESET_ALL)
    print("--------------------------------------------")
    print()

def perpendicular_cm_header():
    print(Fore.RED + "  _____                               _ _            _               __       __  " + Style.RESET_ALL)
    print(Fore.GREEN + " |  __ \                             | (_)          | |             / /       \ \ " + Style.RESET_ALL)
    print(Fore.YELLOW + " | |__) |__ _ __ _ __   ___ _ __   __| |_  ___ _   _| | __ _ _ __  | |_ __ ___ | |" + Style.RESET_ALL)
    print(Fore.BLUE + " |  ___/ _ \ '__| '_ \ / _ \ '_ \ / _` | |/ __| | | | |/ _` | '__| | | '_ ` _ \| |" + Style.RESET_ALL)
    print(Fore.MAGENTA + " | |  |  __/ |  | |_) |  __/ | | | (_| | | (__| |_| | | (_| | |    | | | | | | | |" + Style.RESET_ALL)
    print(Fore.CYAN + " |_|   \___|_|  | .__/ \___|_| |_|\__,_|_|\___|\__,_|_|\__,_|_|    | |_| |_| |_| |" + Style.RESET_ALL)
    print(Fore.RED + "                | |                                                 \_\       /_/ " + Style.RESET_ALL)
    print(Fore.GREEN + "                |_|                                                               " + Style.RESET_ALL)
    print("----------------------------------------------------------------------------------")
    print()

main_header()
clr_console()
main_header()
osinfo()

def loading():
    total = 0
    for value in track(range(100), description="Working on it..."):
        time.sleep(0.005)
        total += 1

def main_menu():
    print(Fore.YELLOW + "No fractions and negative numbers, please!" + Style.RESET_ALL)
    print(Fore.YELLOW + "This program is licensed under The MIT License." + Style.RESET_ALL)
    print()
    print("Which operation would you like to perform?")
    print()
    print("01. Addition")
    print("02. Subtraction")
    print("03. Multiplication")
    print("04. Division")
    print("05. Average")
    print("06. Mean")
    print("07. Mode")
    print("08. Median")
    print("09. Speed (km/h)")
    print("10. Distance (km)")
    print("11. Time (hrs)")
    print("12. Speed (m/s)")
    print("13. Distance (m)")
    print("14. Time (sec)")
    print("15. km/h to m/s")
    print("16. m/s to km/h")
    print("17. km to m")
    print("18. m to km")
    print("19. hrs to sec")
    print("20. sec to hrs")
    print("21. Hypotenuse (m)")
    print("22. Base (m)")
    print("23. Perpendicular (m)")
    print("24. Hypotenuse (cm)")
    print("25. Base (cm)")
    print("26. Perpendicular (cm)")
    print()
    print("0. Exit")
    print("A. Visit my website")
    print("B. Visit the GitHub repository")
    print()

    user_choice = input("Enter the number corresponding to the operation you want to perform: \t")
    clr_console()

    if user_choice == "0":
        main_header()
        loading()
        time.sleep(0.5)
        clr_console()
        sys.exit()
    elif user_choice == "A":
        main_header()
        loading()
        time.sleep(0.5)
        clr_console()
        print(Fore.YELLOW + "Copy the following link and paste it in your browser (under 50 secs)." + Style.RESET_ALL)
        print(Fore.BLUE + "https://aadityas.rf.gd/" + Style.RESET_ALL)
        time.sleep(50)
        main_header()
        osinfo()
        main_menu()
    elif user_choice == "B":
        main_header()
        loading()
        time.sleep(0.5)
        clr_console()
        print(Fore.YELLOW + "Copy the following link and paste it in your browser (under 50 secs)." + Style.RESET_ALL)
        print(Fore.BLUE + "https://github.com/somecoderithink/mathzapp" + Style.RESET_ALL)
        time.sleep(50)
        main_header()
        osinfo()
        main_menu()
    elif user_choice == "1":
        addition_header()
        result = add_numbers()
        clr_console()
        addition_header()
        loading()
        time.sleep(0.5)
        clr_console()
        addition_header()
        print(f"Sum of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "01":
        addition_header()
        result = add_numbers()
        clr_console()
        addition_header()
        loading()
        time.sleep(0.5)
        clr_console()
        addition_header()
        print(f"Sum of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "2":
        subtraction_header()
        result = find_difference()
        clr_console()
        subtraction_header()
        loading()
        time.sleep(0.5)
        clr_console()
        subtraction_header()
        print(f"Difference between the two numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "02":
        subtraction_header()
        result = find_difference()
        clr_console()
        subtraction_header()
        loading()
        time.sleep(0.5)
        clr_console()
        subtraction_header()
        print(f"Difference between the two numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "3":
        multiplication_header()
        result = multiply_numbers()
        clr_console()
        multiplication_header()
        loading()
        time.sleep(0.5)
        clr_console()
        multiplication_header()
        print(f"Product of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "03":
        multiplication_header()
        result = multiply_numbers()
        clr_console()
        multiplication_header()
        loading()
        time.sleep(0.5)
        clr_console()
        multiplication_header()
        print(f"Product of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "4":
        division_header()
        perform_division()
        print()
        return_menu()
    elif user_choice == "04":
        division_header()
        perform_division()
        print()
        return_menu()
    elif user_choice == "5":
        average_header()
        result = calculate_average()
        clr_console()
        average_header()
        loading()
        time.sleep(0.5)
        clr_console()
        average_header()
        if result is not None:
            print(f"Average of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "5":
        average_header()
        result = calculate_average()
        clr_console()
        average_header()
        loading()
        time.sleep(0.5)
        clr_console()
        average_header()
        if result is not None:
            print(f"Average of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "6":
        mean_header()
        result = calculate_mode()
        clr_console()
        mode_header()
        loading()
        time.sleep(0.5)
        clr_console()
        mode_header()
        if result is not None:
            print(f"Mean of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "06":
        mean_header()
        result = calculate_mode()
        clr_console()
        mode_header()
        loading()
        time.sleep(0.5)
        clr_console()
        mode_header()
        if result is not None:
            print(f"Mean of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "7":
        mode_header()
        result = calculate_mode()
        clr_console()
        mode_header()
        loading()
        time.sleep(0.5)
        clr_console()
        mode_header()
        if result is not None:
            print(f"Mode of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "07":
        mode_header()
        result = calculate_mode()
        clr_console()
        mode_header()
        loading()
        time.sleep(0.5)
        clr_console()
        mode_header()
        if result is not None:
            print(f"Mode of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "8":
        median_header()
        result = calculate_median()
        clr_console()
        median_header()
        loading()
        time.sleep(0.5)
        clr_console()
        median_header()
        if result is not None:
            print(f"Median of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "08":
        median_header()
        result = calculate_median()
        clr_console()
        median_header()
        loading()
        time.sleep(0.5)
        clr_console()
        median_header()
        if result is not None:
            print(f"Median of the numbers: ", Fore.GREEN + f"{result}" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "9":
        km_speed_header()
        result = km_speed()
        clr_console()
        km_speed_header()
        loading()
        time.sleep(0.5)
        clr_console()
        km_speed_header()
        if result is not None:
            print("The speed is: ", Fore.GREEN + f"{result} km/h" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "09":
        km_speed_header()
        result = km_speed()
        clr_console()
        km_speed_header()
        loading()
        time.sleep(0.5)
        clr_console()
        km_speed_header()
        if result is not None:
            print("The speed is: ", Fore.GREEN + f"{result} km/h" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "10":
        distance_km_header()
        result = distance_km()
        clr_console()
        distance_km_header()
        loading()
        time.sleep(0.5)
        clr_console()
        distance_km_header()
        if result is not None:
            print("The distance in km is: ", Fore.GREEN + f"{result} km" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "11":
        time_hrs_header()
        result = time_hrs()
        clr_console()
        time_hrs_header()
        loading()
        time.sleep(0.5)
        clr_console()
        time_hrs_header()
        if result is not None:
            print("The time in hrs is: ", Fore.GREEN + f"{result} hrs" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "12":
        m_speed_header()
        result = m_speed()
        clr_console()
        m_speed_header()
        loading()
        time.sleep(0.5)
        clr_console()
        m_speed_header()
        if result is not None:
            print("The speed in m/s is: ", Fore.GREEN + f"{result} m/s" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "13":
        distance_m_header()
        result = distance_m()
        clr_console()
        distance_m_header()
        loading()
        time.sleep(0.5)
        clr_console()
        distance_m_header()
        if result is not None:
            print("The distance in m is: ", Fore.GREEN + f"{result} m" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "14":
        time_sec_header()
        result = time_sec()
        clr_console()
        time_sec_header()
        loading()
        time.sleep(0.5)
        clr_console()
        time_sec_header()
        if result is not None:
            print("The time in sec is: ", Fore.GREEN + f"{result} sec" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "15":
        speed_km_to_m_header()
        result = speed_km_m()
        clr_console()
        speed_km_to_m_header()
        loading()
        time.sleep(0.5)
        clr_console()
        speed_km_to_m_header()
        if result is not None:
            print("The speed in m/s is: ", Fore.GREEN + f"{result} m/s" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "16":
        speed_m_to_km_header()
        result = speed_m_km()
        clr_console()
        speed_m_to_km_header()
        loading()
        time.sleep(0.5)
        clr_console()
        speed_m_to_km_header()
        if result is not None:
            print("The speed in km/h is: ", Fore.GREEN + f"{result} km/h" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "17":
        km_to_m_header()
        result = km_to_m()
        clr_console()
        km_to_m_header()
        loading()
        time.sleep(0.5)
        clr_console()
        km_to_m_header()
        if result is not None:
            print("The distance in m is: ", Fore.GREEN + f"{result} m" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "18":
        m_to_km_header()
        result = m_to_km()
        clr_console()
        m_to_km_header()
        loading()
        time.sleep(0.5)
        clr_console()
        m_to_km_header()
        if result is not None:
            print("The distance in km is: ", Fore.GREEN + f"{result} km" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "19":
        hrs_to_sec_header()
        result = hrs_to_sec()
        clr_console()
        hrs_to_sec_header()
        loading()
        time.sleep(0.5)
        clr_console()
        hrs_to_sec_header()
        if result is not None:
            print("The time in sec is: ", Fore.GREEN + f"{result} sec" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "20":
        sec_to_hrs_header()
        result = sec_to_hrs()
        clr_console()
        sec_to_hrs_header()
        loading()
        time.sleep(0.5)
        clr_console()
        sec_to_hrs_header()
        if result is not None:
            print("The time in hrs is: ", Fore.GREEN + f"{result} hrs" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "21":
        hypotenuse_m_header()
        result = hypotenuse_m()
        clr_console()
        hypotenuse_m_header()
        loading()
        time.sleep(0.5)
        clr_console()
        hypotenuse_m_header()
        if result is not None:
            print("The length of the hypotenuse in m is: ", Fore.GREEN + f"{result} m" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "22":
        base_m_header()
        result = base_m()
        clr_console()
        base_m_header()
        loading()
        time.sleep(0.5)
        clr_console()
        base_m_header()
        if result is not None:
            print("The length of the base in m is: ", Fore.GREEN + f"{result} m" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "23":
        perpendicular_m_header()
        result = perpendicular_m()
        clr_console()
        perpendicular_m_header()
        loading()
        time.sleep(0.5)
        clr_console()
        perpendicular_m_header()
        if result is not None:
            print("The length of the perpendicular in m is: ", Fore.GREEN + f"{result} m" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "24":
        hypotenuse_cm_header()
        result = hypotenuse_cm()
        clr_console()
        hypotenuse_cm_header()
        loading()
        time.sleep(0.5)
        clr_console()
        hypotenuse_cm_header()
        if result is not None:
            print("The length of the hypotenuse in cm is: ", Fore.GREEN + f"{result} cm" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "25":
        base_cm_header()
        result = base_cm()
        clr_console()
        base_cm_header()
        loading()
        time.sleep(0.5)
        clr_console()
        base_cm_header()
        if result is not None:
            print("The length of the base in cm is: ", Fore.GREEN + f"{result} cm" + Style.RESET_ALL)
        print()
        return_menu()
    elif user_choice == "26":
        perpendicular_cm_header()
        result = perpendicular_cm()
        clr_console()
        perpendicular_cm_header()
        loading()
        time.sleep(0.5)
        clr_console()
        perpendicular_cm_header()
        if result is not None:
            print("The length of the perpendicular in cm is: ", Fore.GREEN + f"{result} cm" + Style.RESET_ALL)
        print()
        return_menu()
    else:
        print(Fore.RED + "Invalid choice. Please try again" + Style.RESET_ALL)
        time.sleep(5)
        clr_console()
        main_header()
        clr_console()
        main_header()
        osinfo()
        main_menu()
    print()

def add_numbers():
    user_input = input("Enter numbers separated by commas to be added: \t")
    numbers = user_input.split(",")
    total = 0

    for number in numbers:
        try:
            num = float(number)
            total += num
        except ValueError:
            print(Fore.RED + f"Invalid number: '{number}' is not a valid number." + Style.RESET_ALL)
            time.sleep(5)
            clr_console()
            main_header()
            clr_console()
            main_header()
            osinfo()
            main_menu()

    return total

def find_difference():
    user_input = input("Enter two numbers separated by a comma: \t")
    numbers = user_input.split(",")

    if len(numbers) != 2:
        print(Fore.RED + "Please enter exactly two numbers separated by a comma." + Style.RESET_ALL)

        return

    try:
        num1, num2 = map(float, numbers)
        result = num1 - num2
    except ValueError:
        print(Fore.RED + "Invalid input: Please enter two valid numbers." + Style.RESET_ALL)
        time.sleep(5)
        clr_console()
        main_header()
        clr_console()
        main_header()
        osinfo()
        main_menu()
    return

    return result

def multiply_numbers():
    user_input = input("Enter numbers separated by commas to be multiplied: \t")
    numbers = user_input.split(",")
    total = 1

    for number in numbers:
        try:
            num = float(number)
            total *= num
        except ValueError:
            print(Fore.RED + f"Invalid number: '{number}' is not a valid number." + Style.RESET_ALL)
            time.sleep(5)
            clr_console()
            main_header()
            clr_console()
            main_header()
            osinfo()
            main_menu()

    return total

def calculate_average():
    user_input = input("Enter the numbers separated by commas to find their average: \t")
    numbers = user_input.split(",")
    total = 0

    for number in numbers:
        try:
            num = float(number)
            total += num
        except ValueError:
            print(Fore.RED + f"Invalid number: '{number}' is not a valid number." + Style.RESET_ALL)
            time.sleep(5)
            clr_console()
            main_header()
            clr_console()
            main_header()
            osinfo()
            main_menu()

    average = total / len(numbers)
    return total

def calculate_mean():
    user_input = input("Enter the numbers separated by commas to find their mean: \t")
    numbers = user_input.split(",")
    total = 0

    for number in numbers:
        try:
            num = float(number)
            total += num
        except ValueError:
            print(Fore.RED + f"Invalid number: '{number}' is not a valid number." + Style.RESET_ALL)
            time.sleep(5)
            clr_console()
            main_header()
            clr_console()
            main_header()
            osinfo()
            main_menu()

    average = total / len(numbers)
    return total

def perform_division():
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))

    clr_console()
    division_header()
    loading()
    time.sleep(0.5)
    clr_console()
    division_header()

    if divisor == 0:
        print(Fore.RED + "Error: Division by zero is not allowed." + Style.RESET_ALL)
        time.sleep(5)
        clr_console()
        main_header()
        clr_console()
        main_header()
        osinfo()
        main_menu()
    else:
        quotient = int(dividend / divisor)
        remainder = dividend % divisor
        print("The quotient is", Fore.GREEN + f"{quotient}" + Style.RESET_ALL, "and the remainder is", Fore.GREEN + f"{remainder}" + Style.RESET_ALL)

def calculate_mode():
    user_input = input("Enter numbers separated by commas to find their mode: \t")
    numbers = user_input.split(",")

    if len(numbers) == 0:
        print(Fore.RED + "Please enter at least one number to calculate the mode." + Style.RESET_ALL)
        time.sleep(5)
        clr_console()
        main_header()
        clr_console()
        main_header()
        osinfo()
        main_menu()
        return

    try:
        numbers = [float(number) for number in numbers]
        mode = statistics.mode(numbers)
        return mode
    except (ValueError, statistics.StatisticsError):
        print(Fore.RED + "Invalid input or no mode found." + Style.RESET_ALL)
        time.sleep(5)
        clr_console()
        main_header()
        clr_console()
        main_header()
        osinfo()
        main_menu()
    return None

def calculate_median():
    user_input = input("Enter numbers separated by commas to find their median: \t")
    numbers = user_input.split(",")

    if len(numbers) == 0:
        print(Fore.RED + "Please enter at least one number to calculate the median." + Style.RESET_ALL)
        time.sleep(5)
        clr_console()
        main_header()
        clr_console()
        main_header()
        osinfo()
        main_menu()
        return

    try:
        numbers = [float(number) for number in numbers]
        median = statistics.median(numbers)
        return median
    except (ValueError, statistics.StatisticsError):
        print(Fore.RED + "Invalid input or no median found." + Style.RESET_ALL)
        time.sleep(5)
        clr_console()
        main_header()
        clr_console()
        main_header()
        osinfo()
        main_menu()
    return None

def km_speed():
    distance = float(input("Enter the distance (in km): \t"))
    timez = float(input("Enter the time (in hrs): \t"))

    speed = distance / timez
    return speed

def m_speed():
    distance = float(input("Enter the distance (in m): \t"))
    timez = float(input("Enter the time (in sec): \t"))

    speed = distance / timez
    return speed

def distance_km():
    speed = float(input("Enter the speed (in km/h): \t"))
    time = float(input("Enter the time (in hrs): \t"))

    distance = speed * time
    return distance

def distance_m():
    speed = float(input("Enter the speed (in m/s): \t"))
    time = float(input("Enter the time (in sec): \t"))

    distance = speed * time
    return distance

def return_menu():
    return_ask = input("Do you want to return to the main menu? (y/n): \t")

    if return_ask == "y":
        clr_console()
        main_header()
        main_menu()
    elif return_ask == "n":
        clr_console()
        main_header()
        loading()
        clr_console()
        sys.exit()

def speed_km_m():
    km_speed = float(input("Enter the speed (in km/h): \t"))
    m_speed = "{:.2f}".format(km_speed * 5/18)
    return m_speed

def speed_m_km():
    m_speed = float(input("Enter the speed (in m/s): \t"))
    km_speed = "{:.2f}".format(m_speed * 18/5)
    return km_speed

def time_hrs():
    distance = float(input("Enter the distance (in km): \t"))
    speed = float(input("Enter the speed (in km/h): \t"))

    time = "{:.2f}".format(distance / speed)
    return time

def time_sec():
    distance = float(input("Enter the distance (in m): \t"))
    speed = float(input("Enter the speed (in m/s): \t"))

    time = "{:.2f}".format(distance / speed)
    return time

def km_to_m():
    km = float(input("Enter the distance in km: \t"))
    m = km * 1000
    return m

def m_to_km():
    m = float(input("Enter the distance in m: \t"))
    km = m / 1000
    return km

def hrs_to_sec():
    hrs = float(input("Enter the time in hrs: \t"))
    sec = hrs * 3600
    return sec

def sec_to_hrs():
    sec = float(input("Enter the time in sec: \t"))
    hrs = sec / 3600
    return hrs

def hypotenuse_m():
    base = float(input("Enter the length of the base (in m): \t"))
    perpendicular = float(input("Enter the length of the perpendicular (in m): \t"))

    hypotenuse = math.sqrt(base ** 2 + perpendicular ** 2)
    return hypotenuse

def base_m():
    hypotenuse = float(input("Enter the length of the hypotenuse (in m): \t"))
    perpendicular = float(input("Enter the length of the perpendicular (in m): \t"))

    base = math.sqrt(hypotenuse ** 2 - perpendicular ** 2)
    return base

def perpendicular_m():
    hypotenuse = float(input("Enter the length of the hypotenuse (in m): \t"))
    base = float(input("Enter the length of the base (in m): \t"))

    perpendicular = math.sqrt(hypotenuse ** 2 - base ** 2)
    return perpendicular

def hypotenuse_cm():
    base = float(input("Enter the length of the base (in cm): \t"))
    perpendicular = float(input("Enter the length of the perpendicular (in cm): \t"))

    hypotenuse = math.sqrt(base ** 2 + perpendicular ** 2)
    return hypotenuse

def base_cm():
    hypotenuse = float(input("Enter the length of the hypotenuse (in cm): \t"))
    perpendicular = float(input("Enter the length of the perpendicular (in cm): \t"))

    base = math.sqrt(hypotenuse ** 2 - perpendicular ** 2)
    return base

def perpendicular_cm():
    hypotenuse = float(input("Enter the length of the hypotenuse (in cm): \t"))
    base = float(input("Enter the length of the base (in cm): \t"))

    perpendicular = math.sqrt(hypotenuse ** 2 - base ** 2)
    return perpendicular

main_menu()
#######################################################################################################################