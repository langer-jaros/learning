###### description" content="Knowledge extracted from youtube video.
# HTML5 and CSS3 full course - freeCodeCamp.org
[Link to the video.](https://youtu.be/mU6anWqZJcc)
## Images knowledge [ 16) Images - 51:17 ]
#### Sites with free images
    [pixabay](https://pixabay.com)
    [pexels](https://www.pexels.com/)
    [gratisography](https://gratisography.com/)
## 74) External Resources - 04:52:57
    [Color pallete](https://coolors.co/)
## 77) Percent Values - 05:02:13 | 78) Em Values - 05:05:44 | 79) Rem Values - 05:11:42
    percents depend on parant</p>
    ems depend on parant</p>
    rems depend on root of document</p>
    *{
        margin 0;
        padding 0;
        box-sizing: border-box;
    }
## 86) Google Fonts - 05:39:23</h2>
    [Fonts google](https://fonts.google.com/)
## 88) Text-Align And Text-Indent - 05:53:30
    text-indent: 50px
## 94) Border-Radius, Negative Margin - 06:23:57
    p {
        border-radius: 50%;
    }
## 99) Mobile Navbar Example - 06:48:11
/<a href="#">#</a>
## 102) Display:none, Opacity, Visibility - 07:09:29
    opacity | opacity-5 | opacity-0
    backround-repeat: round
## 111) Background Image Shortcuts Combined - 07:56:49
    .header{
        backround: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
        url("./big.jpeg")center/cover no-repeat fixed;
    }
## 112) Linear-Gradient Colorzilla - 08:06:56
[css gradient generator](https://www.colorzilla.com/gradient-editor/)
# Den druhý
## 116) Position Static - 08:25:59 | 117) Position Relative - 08:30:44  118) Position Absolute - 08:33:18 | 119) Position Fixed - 08:38:4
    oo
## 122) ::Before And ::After Pseudo Elements - 09:06:04
    p::before{ content: "hello "; display: block;}
## 125) Descendant Child Selectors - 09:31:07
    div h1 {} | div > h1 {}
## 126) First Line And First Letter - 09:35:50
    p::first-line {} | p::first-letter
## 127) :Hover Pseudo-Class Selector - 09:36:56
    p:hover
## 129) :Root Preudo-Class Selectors - 09:44:36
    p:root - good for responsive size of text
[Tady jsem zatím skončil.](https://youtu.be/mU6anWqZJcc?t=35497)
## 131) Transform:transition() - 09:52:17
    display: inline-block;
    transform: translate(px, px)
    transform: scale( $num, $num)
    transform: rotateX|Y|Z($(num)deg) 
    transform: skew(40deg, 60deg)
##  135) Transition Property - 10:06:31
    div:hover {
        backround: coral;
    }
    .three{
        transition-property: backround;
        transition-duration: 4s;
    }
    transition-delay: 4s;
    transition: {property} {lenght} {delay  
    transition: all 4s function 5s;
    }
## 138) Transition-Timing Function - 10:16:36
    ease = default
    .sth{
        transition-timig-function: ease;
    }
    ease | linear | ease-in | ease-out | ease-in-out
## 139) Animation - 10:25:51
    @keyframes  move {
        0%{
            transform: translateX
        } 
        50%{
            transform: translateX
        }
    }
    .div {
        animation-name: move;
        animation-duration: 10s;
        animation-iteration-count: 2;
        animation: move duration count;
        animation: move 5s infinite;
    }
## 140) Animation-Fill-Mode - 10:35:51
    animation-fill-mode: forwards;
## 142) Css Variables - 10:41:32
    :root{
        --primaryColor: #f15025;
    }
    .div{
        color:var(--primaryColor)
    }
## 143) Font-Awesome Icons - 10:56:19    
fontawesome.com
## 144) Text-Shadow Box-Shadow - 11:07:55
    box-shadow generator

can i use css

## 145) Browser Prefixes - 11:14:44
    autoprefixer css online
##  146) Semantic Tags - 11:19:23
    semantic HTML