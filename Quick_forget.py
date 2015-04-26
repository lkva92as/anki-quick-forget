from aqt import mw
from aqt.reviewer import Reviewer
from anki.hooks import wrap
from aqt.utils import tooltip

def keyHandler(self, evt, _old):
    key = unicode(evt.text())
    if key == "$":
        self.onForget()
    else:
        return _old(self, evt)

Reviewer._keyHandler = wrap(Reviewer._keyHandler, keyHandler, "around")

def onForget(self):
    self.mw.checkpoint(_("Forget"))
    self.mw.col.sched.forgetCards(
        [c.id for c in self.card.note().cards()])
    tooltip(_("Note rescheduled as new"))
    self.mw.reset()

Reviewer.onForget = onForget
