au BufNewFile,BufRead *.py
            \ set foldmethod=indent

autocmd FileType python map <buffer> <F9> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F9> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>

let g:formatter_yapf_style = 'pep8'
let g:formatters_python = ['yapf']
au BufWrite *.py :Autoformat
