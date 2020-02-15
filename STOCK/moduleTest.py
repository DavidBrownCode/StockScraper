import platform
import nasdaqModule

for x in nasdaqModule.nasdaqTickers:
    print(x)

c = dir(nasdaqModule)
print(c)