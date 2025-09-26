<!-- 部长自我介绍 -->
<template>
  <div class="background"></div>
  <RecruitAnimation ref="bangLottery" style="width: 100vh; height: 100vw;" :theme="theme"/>
  <InfoDisplay ref="infoDisplay" :name="name" :avatar-url="avatarUrl" :shumeiniang-image="shumeiniangImage"/>
</template>

<script>
import RecruitAnimation from '@/components/RecruitAnimation.vue'; 
import InfoDisplay from '@/components/InfoDisplay.vue';

const DIRECTORS = [
  {name: "林子煊", avatarUrl: "/avatar/azusa.jpeg", theme: "GenshinImpact", shumeiniangImage: "guitar2"},
  {name: "张家诚", avatarUrl: "/avatar/mugi.jpeg", theme: "Arknights", shumeiniangImage: "keyboard"},
  {name: "袁靖", avatarUrl: "/avatar/mio.jpeg", theme: "WutheringWaves", shumeiniangImage: "bass"},
  {name: "杨浩天", avatarUrl: "/avatar/ritsu.jpeg", theme: "PJSK", shumeiniangImage: "drum"},
  {name: "郭逸戈", avatarUrl: "/avatar/yui.jpeg", theme: "BanGDream", shumeiniangImage: "guitar1"},
  {name: "江昆", avatarUrl: "", theme: "Wuhuamixin", shumeiniangImage: "ice-cream"},
  {name: "宋宇阳", avatarUrl: "", theme: "GenshinImpact", shumeiniangImage: "bread"},
  {name: "张一航", avatarUrl: "", theme: "Arknights", shumeiniangImage: "cake"},
  {name: "杨尚昕", avatarUrl: "", theme: "DeltaForce", shumeiniangImage: "air-plane"},
  {name: "陈超", avatarUrl: "", theme: "GenshinImpact", shumeiniangImage: "coffee"},
];

export default {
  name: 'App',
  components: {
    RecruitAnimation,
    InfoDisplay
  },
  data() {
    return {
      name: '', // 人员姓名
      theme: '',
      avatarUrl: '',
      index: -1,
      shumeiniangImage: '',
      playingAnim: false,
      fullScreen: false
    }
  },
  methods: {
    enterFullscreen() {
        const element = document.documentElement; // 整个页面全屏
        const requestMethod =
            element.requestFullscreen ||
            element.webkitRequestFullscreen ||
            element.mozRequestFullScreen ||
            element.msRequestFullscreen;

        if (requestMethod) {
            requestMethod.call(element).catch((err) => {
                console.error("全屏失败:", err);
                this.enableFullScreen = false; // 失败时重置状态
            });
        }
    },

    exitFullscreen() {
        const exitMethod =
            document.exitFullscreen ||
            document.webkitExitFullscreen ||
            document.mozCancelFullScreen ||
            document.msExitFullscreen;

        if (exitMethod) {
            exitMethod.call(document);
        }
    },
    displayLotteryAnim(name, avatarUrl, theme, shumeiniangImage) {
      const self = this;

      this.playingAnim = true;
      // console.log(this.$refs.infoDisplay);
      this.$refs.infoDisplay.hide();
      this.theme = theme;
      this.$nextTick(() => {
        this.name = name;
        this.avatarUrl = avatarUrl;
        this.shumeiniangImage = shumeiniangImage;
        
        this.$refs.bangLottery.play()
          .then(() => {
            self.$refs.infoDisplay.display();
            this.playingAnim = false;
          });
        }
      );
    },

    skipAnimation() {
      this.$refs.bangLottery.reset();
      this.$refs.infoDisplay.display();
      this.playingAnim = false;
    }
  },
  mounted() {
    document.addEventListener('keydown', (e) => {
      if (e.key === " ") {
        this.skipAnimation();
      }
      if (e.key === "ArrowDown") {
        if (this.playingAnim) {
          this.skipAnimation();
        } else {
          if (this.index + 1 >= DIRECTORS.length) return;
          this.index += 1;
          const director = DIRECTORS[this.index];
          this.displayLotteryAnim(director.name, director.avatarUrl, director.theme, director.shumeiniangImage);
        }
      } else if (e.key === "ArrowUp") {
        if (this.index - 1 < 0) return;
        this.index -= 1;
        const director = DIRECTORS[this.index];
        this.displayLotteryAnim(director.name, director.avatarUrl, director.theme, director.shumeiniangImage);
      }
    });

    document.addEventListener('keydown', (e) => {
      // 进入/退出全屏
      if (e.key === 'f' || e.key === 'F') {
        try {
          if (this.fullScreen) {
            this.exitFullscreen();
            this.fullScreen = false;
          } else {
            this.enterFullscreen();
            this.fullScreen = true;
          }
        } catch(e) {
          console.log("It seems you toggled full screen mode manually. Press key 'f' instead.");
        }
      }
    });
  }
}
</script>

<style>
.background {
  width: 100vw;
  height: 100vh;
  top: 0;
  left: 0;
  margin: 0;
  background-size: cover;
  background-image: url("@/assets/bg0.jpeg");
}
</style>
