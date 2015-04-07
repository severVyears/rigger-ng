#!/usr/bin/env python
# -*- coding: utf-8 -*-


import  re , os , string ,  getopt ,sys , unittest,logging


if __name__ == '__main__':

    root  = os.path.dirname(os.path.realpath(__file__))
    root  = os.path.dirname(root)
    sys.path.append(os.path.join(root,"src") )

    logging.basicConfig(level=logging.DEBUG,filename='test.log')
    import interface,impl
    impl.setup()

    from impl_tc.yaml_tc  import *
    from utls_tc.tpl_tc   import *
    from impl_tc.vars_tc  import *
    from impl_tc.args_tc  import *
    from impl_tc.cmd_tc   import *
    # from res_tc.mysql_tc  import *
    # from res_tc.files_tc  import *
    # from res_tc.daemon_tc  import *
    # from res_tc.share_dict_tc  import *
    # from res_tc.shell_tc  import *
    from res_tc.crontab_tc  import *
    from res_tc.syslog_tc   import *

    unittest.main()
