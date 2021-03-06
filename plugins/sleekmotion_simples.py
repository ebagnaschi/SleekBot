"""
    bmotion_simples.py - A port of the bmotion simple stuffs.
    Copyright (C) 2007 Kevin Smith.
    Original logic copyright of bMotion project.

    SleekBot is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    SleekBot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this software; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import logging

class sleekmotion_simples(object):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config
        
        
        self.bot.botplugin['sleekmotion'].addValues('blessyous', [
            "gesuntheit",
            "bless you",
            "Bless you",
            "/hands %% a tissue",
            "e%REPEAT{2:5:w}%|*wipe*",
            "hehe, someone must be talking about you %VAR{smiles}",
            "good thing I bought this haz-mat suit",
            "Rogue bogey!",
            "/ducks",
            '/hides behind %ruser',
            "Great. Now I'm gonna get a cold %VAR{unsmiles}",
            "Eek. Don't give it to me",
            "%% - I recommend %VAR{sillyThings}"])
        
        self.bot.botplugin['sleekmotion'].addValues('goonthens', ["sssh sekrit",  "go on then", "oh go on then", "ok then, but don't tell anyone"])
        
        self.bot.botplugin['sleekmotion'].addValues('here_responses',[        "%VAR{nos}"])
        
        self.bot.botplugin['sleekmotion'].addValues('notbots', ["no I'm not",
          "am not %VAR{unsmiles}",
          "am not",
          "LIES.",
          "SILENCE%FUNC{colen}",
          "LIES, ALL LIES%|(unless a witness steps forward)",
          "/smothers %%%|shh, someone will hear",
          "shh%|sekrit"])
            
        self.about = "'bmotion_simples' Simple ports of all the bmotion simple plugins. \nBased on the bMotion plugin.\nWritten by Kevin Smith"
        t = self.bot.botplugin['sleekmotion'].registerTrigger
        t('sneeze', '^\*?(/sneezes|.hatsjoe|wachoo|sneezes|.a+tchoo+)', 60, '%VAR{blessyous}')
        t("zzz","^zzz+",50, '%VAR{handcoffees}')
        t("takethat","^take that!",60, ["and party!","and party"])
        t("wrongsmiley",'{^L\($}', 60, ["taunt","fail","WORST. SMILEY. EVER.","try realigning your fingers for that one","E_SMILEY"])
        t("bisto","^ahh+$",10, "Bisto!")
        t("thinkso","^(no, )?(i|I) do(n't| not) think so",10, ["Mr Negative","I DO think so.", "and what would you know?"])
        t("littlebit", "(what, )?not even a little bit", 40, "%VAR{goonthens}")
        t("nn", "(nn|gn|nite|night|nite ?nite),? (%botnicks|all)!*$", 100, ["nn %VAR{unsmiles}", "nn", "nite", "night", "nn %%", "sleep well", "sweet dreams"])
        t("here","^any ?(one|body) (here|alive|talking)", 40, "%VAR{here_responses}")

        t("notbot", "%botnicks('s| is) a bot", 60, "%VAR{notbots}")

        t("arebot", "((is %botnicks a bot)|(are you a bot,? %botnicks)|(^%botnicks:? are you a bot))", 60, "%VAR{nos}")
        t("rules", "(%botnicks|bmotion|sleek|sleekmotion) (rock(s|z)|own(s|z)|rule?(s|z)|pwn(s|z))", 100, "%VAR{thanks}")
        #from simple_general.tcl
        t("url-img", "(http|ftp)://([[:alnum:]]+\.)+[[:alnum:]]{2,3}.+\.(jpg|jpeg|gif|png)", 25, "%VAR{rarrs}") 
        t("ali g", "^((aiii+)|wikkid|innit|respect|you got me mobile|you iz)", 40, "%VAR{aiis}") 
        t("wassup", "^wa+((ss+)|(zz+))(a|u)+p+!*$", 40, "wa%REPEAT{4:12:a}up!")
        t("oops", "^(oops|who+ps|whups|doh |d\'oh)", 40, "%VAR{ruins}")
        t("bof", "^bof$", 30, [ "alors", "%VAR{FRENCH}"])
        t("alors", "^alors$", 30, [ "bof", "%VAR{FRENCH}"]) 
        t("bonjour", "bonjour", 20, "%VAR{FRENCH}")
        t("foo", "^foo$", 30, "bar")
        t("bar", "^bar$", 30, "foo") 
        t("moo", "^mooo*!*$", 40, "%VAR{moos}")
        t(":(", "^((:|;|=)(\\(|\\[))$", 40, "%VAR{boreds}")
        t("bored", "i'm bored", 40, "%VAR{boreds}")
        t("transform", "^%botnicks:?,? transform and roll out", 100, [ "/transforms into %VAR{sillyThings} and rolls out"])
        t("didn't!", "^i didn'?t!?$", 40, "%VAR{ididntresponses}")
        t("ow", "^(ow+|ouch|aie+)!*$", 50, "%VAR{awwws}")
        t("dude", "^Dude!$", 40, "%VAR{sweet}")
        t("sweet", "^Sweet!$", 40, "%VAR{dude}") 
        t("asl-catch", "[0-9]+%slash[mf]%slash.+", 75, "%VAR{greetings}")
        t("sing-catch", "^#.+#$", 40, [ "no singing%colen", "shh%colen"] )
        t("seven", "^7[?!.]?$", 40, [ "7!", "7 %VAR{smiles}", "wh%REPEAT{3:7:e} 7!"] )
        t("mmm", "mmm+ $botnicks", 25, "%VAR{smiles}")
        #t("no-mirc", "mirc", 5, [ "mIRC < irssi", "use irssi", "mmm irssi", "irssi > *", "/fires %% into the sun"] )
        #t("no-bitchx", "bitchx", 5, [ "bitchx < irssi", "use irssi", "mmm irssi", "irssi > *", "/fires %% into the sun"] )
        #t("no-trillian", "trillian", 5, [ "trillian < irssi", "use trillian + bitlbee", "mmm irssi", "irssi > *", "/fires %% into the sun"] )
        t("right", "%botnicks: (i see|ri+ght|ok|all? ?right|whatever)", 60, [ "it's true %VAR{unsmiles}", "it's true%colen", "yes", "what", "you don't believe me?"] )
        t("hal", "%botnicks:?,?;? open the cargo bay doors?", 70, [ "I'm sorry %%, I can't do that."] )
        t("only4", "^only [0-9]+", 80, [ "well actually %NUMBER{100}", "that's quite a lot", "that's not very many", "well that's usually enough to get me functioning"] )
        
        #some complex which are simple:
        t("shocked", "^((((=|:|;)-?(o|0))|(!+))|blimey|crumbs|i say)$", 40, "%VAR{shocked}")
        t("wrong console(tm)", "^rm|^cp|^su( -)?$|^make$|^ls", 60, ["yay! %% can't get it right", "why don't you tell us your password as well?", "try the other window", "try 'rm -rf /' as root", "Would you like a hand?", "twit.", "%% is t3h l337 h4x0R!"])