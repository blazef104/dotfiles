set tabstop=4
set shiftwidth=4
set softtabstop=0 noexpandtab
" Vimplug section
" Specify a directory for plugins
" - For Neovim: ~/.local/share/nvim/plugged
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.local/share/nvim/plugged')

" Make sure you use single quotes

" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
"Plug 'junegunn/vim-easy-align'

" Any valid git URL is allowed
"Plug 'https://github.com/junegunn/vim-github-dashboard.git'

" Multiple Plug commands can be written in a single line using | separators
"Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'

Plug 'tpope/vim-sensible'
Plug 'scrooloose/nerdtree'
Plug 'mhartington/oceanic-next' 
Plug 'kien/rainbow_parentheses.vim'
Plug 'mhinz/vim-startify'

Plug 'ryanoasis/vim-devicons'

" Initialize plugin system
call plug#end()

" Set a nerdfornt needed for devicons
set guifont=DroidSansMono\ Nerd\ Font\ 11
" Theme oceanic-next
set termguicolors
syntax enable
colorscheme OceanicNext

" Rainbow Parentheses always on
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces

" Startup nerdtree when starting vim with no file specified
" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

let g:webdevicons_enable = 1
