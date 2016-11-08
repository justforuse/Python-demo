import module1
module1.func("world")
module1.func("cola")

import imp
imp.reload(module1)
module1.func("sprite")
