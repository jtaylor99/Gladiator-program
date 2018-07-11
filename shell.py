import core


def get_name_and_assign_stats():
    name_1 = input('What\'s your name?')
    print('Welcome to the Game of Gladiators!', name_1.upper(), '!')
    name_2 = input('What\'s your name?')
    print('Welcome to the Game of Gladiators!', name_2.upper(), '!')
    name_1 = core.new_gladiator(name_1, 100, 0, 10, 20, 1)
    name_2 = core.new_gladiator(name_2, 100, 0, 10, 20, 1)
    return name_1, name_2


def weapons():
    weapons = []


def gladiator_turn(name_1, name_2):
    print('{} turn'.format(name_1['Name'].upper()))
    while True:

        print('>>>>[A]ttack')
        print('>>>>[L]evel up')
        print('>>>>[H]eal')
        print('>>>>[P]ass')
        print('>>>>[Q]uit')
        action = input('{} What would you like to do?'.format(
            name_1['Name'].upper()))
        if action == 'A':
            print(name_1['Name'].upper(), 'Attacks')
            result = core.attack(name_1, name_2)
            if result == 'miss':
                print('{} misses'.format(name_1['Name'],
                                         name_2['Name'].upper()))
                return None
            if result == 'crit':
                print('critical damage!')
                print('{} health is now at:{}'.format(name_2['Name'].upper(),
                                                      name_2['health']))
                return None
            if result == 'hit':
                print('{} health is now at:{}'.format(name_2['Name'].upper(),
                                                      name_2['health']))
                print('{} rage is now {}'.format(name_1['Name'],
                                                 name_1['rage']))
                return None
        if action == 'L':
            result = core.leveled_up(name_1)
            print('{} has leveled up'.format(name_1['Name'], name_2['Name']))
            print('{} is now at level{}'.format(name_1['Name'],
                                                name_1['level']))
            return None
        if action == 'H':
            print(name_1['Name'], 'Heals')
            core.heal(name_1)
            print('{} health is now at:{}'.format(name_1['Name'].upper(),
                                                  name_1['health']))
            return None
        if action == 'P':
            break
        if action == 'Q':
            print('{} has run away'.format(name_1['Name'],
                                           name_2['Name'].upper()))
            quit()

        else:
            print('Please choose a valid option!')


def is_winner(name_1, name_2):
    if name_2['health'] <= 0:
        print('winner:{}'.format(name_1['Name'].upper()))
    if name_1['health'] <= 0:
        print('winner:{}'.format(name_2['Name'].upper()))


def is_dead(name_1, name_2):
    if name_1['health'] <= 0:
        return True
    elif name_2['health'] <= 0:
        return True


def main():
    print('''           _..gggggppppp.._                       
                  _.gd$$$$$$$$$$$$$$$$$$bp._                  
               .g$$$$$$P^^""j$$b""""^^T$$$$$$p.               
            .g$$$P^T$$b    d$P T;       ""^^T$$$p.            
          .d$$P^"  :$; `  :$;                "^T$$b.          
        .d$$P'      T$b.   T$b                  `T$$b.        
       d$$P'      .gg$$$$bpd$$$p.d$bpp.           `T$$b       
      d$$P      .d$$$$$$$$$$$$$$$$$$$$bp.           T$$b      
     d$$P      d$$$$$$$$$$$$$$$$$$$$$$$$$b.          T$$b     
    d$$P      d$$$$$$$$$$$$$$$$$$P^^T$$$$P            T$$b    
   d$$P    '-'T$$$$$$$$$$$$$$$$$$bggpd$$$$b.           T$$b   
  :$$$      .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p._.g.     $$$;  
  $$$;     d$$$$$$$$$$$$$$$$$$$$$$$P^"^T$$$$P^^T$$$;    :$$$  
 :$$$     :$$$$$$$$$$$$$$:$$$$$$$$$_    "^T$bpd$$$$,     $$$; 
 $$$;     :$$$$$$$$$$$$$$bT$$$$$P^^T$p.    `T$$$$$$;     :$$$ 
:$$$      :$$$$$$$$$$$$$$P `^^^'    "^T$p.    lb`TP       $$$;
:$$$      $$$$$$$$$$$$$$$              `T$$p._;$b         $$$;
$$$;      $$$$$$$$$$$$$$;                `T$$$$:Tb        :$$$
$$$;      $$$$$$$$$$$$$$$                        Tb    _  :$$$
:$$$     d$$$$$$$$$$$$$$$.                        $b.__Tb $$$;
:$$$  .g$$$$$$$$$$$$$$$$$$$p...______...gp._      :$`^^^' $$$;
 $$$;  `^^'T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p.    Tb._, :$$$ 
 :$$$       T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.   "^"  $$$; 
  $$$;       `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b      :$$$  
  :$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;     $$$;  
   T$$b    _  :$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;   d$$P   
    T$$b   T$g$$; :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  d$$P    
     T$$b   `^^'  :$$ "^T$$$$$$$$$$$$$$$$$$$$$$$$$$$ d$$P     
      T$$b        $P     T$$$$$$$$$$$$$$$$$$$$$$$$$;d$$P      
       T$$b.      '       $$$$$$$$$$$$$$$$$$$$$$$$$$$$P       
        `T$$$p.   bug    d$$$$$$$$$$$$$$$$$$$$$$$$$$P'        
          `T$$$$p..__..g$$$$$$$$$$$$$$$$$$$$$$$$$$P'          
            "^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$^"            
               "^T$$$$$$$$$$$$$$$$$$$$$$$$$$P^"               
                   """^^^T$$$$$$$$$$P^^^"""
''')
    name_1, name_2 = get_name_and_assign_stats()
    while True:
        gladiator_turn(name_1, name_2)
        if is_dead(name_1, name_2):
            break
        gladiator_turn(name_2, name_1)
        if is_dead(name_1, name_2):
            break
    is_winner(name_1, name_2)


if __name__ == '__main__':
    main()
