from IPython.core.display import clear_output as c_o
class Progress:
  
    def __init__(self, total_iter, start_pos = 0, *args, **kwargs):
        if type(total_iter) is not int:
            raise TypeError("total_iter should be a number, is %s"%type(total_iter))
        if (type(start_pos) is not int) and not(start_pos >= 0 and start_pos <=1):
            raise TypeError("start_pos should be a number or percentage between 0 and 1, is %s"%type(start_pos))

        if start_pos <= 1 and start_pos >= 0:
            start_pos = int(total_iter * start_pos)
        elif start_pos > total_iter:
            raise ValueError("starting excceds endpoint")

        self.total_iter = total_iter
        self.curr_pos = start_pos
        self.start_pos = start_pos
        self.char_comp = "="
        self.char_uncomp = "_"
        self._notify_comp = False
        
        if args:
            self.char_comp = [args[0] if len(args[0]) is 1 else '='][0]
            self.char_uncomp = [args[1] if len(args[1]) is 1 else '_'][0]
        
        if kwargs:
            if 'notify_completion' in kwargs:
                if type(kwargs['notify_completion']) is not type(True):
                    raise ValueError('Kwargs \'notify_completion\' needs to be a bool type, is %s'%type(kwargs['notify_completion']))
                self._notify_comp = kwargs['notify_completion']      
    
    def __str__(self):
        return "instance of Progress with %s progresses out of which %s has already been completed"%(self.total_iter,self.curr_pos)

    def update_progress(self, show_prog = True, incrmt = 1):
        if self.curr_pos == self.total_iter:
            raise ValueError("task already completed, increase total_iter")
        self.curr_pos += incrmt
        if show_prog:
            self._showProgress()
        if self.curr_pos >= self.total_iter:
            self.curr_pos = self.total_iter
            if self._notify_comp:
                print("Task completed successfully")       
            
    def _showProgress(self):
        c_o(wait = True)
        _prog = int(self.curr_pos * 50 / self.total_iter)
        print("|" + '='*_prog + '_'*(50 - _prog) + '| %.2f'%(self.curr_pos * 100 / self.total_iter) + '%')
            