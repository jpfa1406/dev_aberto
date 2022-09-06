#!/usr/bin/env python3
import dev_aberto as dev

if __name__ == '__main__':
    date, name = dev.hello()
    print('Último commit feito em:', date, ' por', name)
