<template>
  <div class="background"></div>
  <RecruitAnimation ref="bangLottery" style="width: 100vh; height: 100vw;" :theme="theme"/>
  <InfoDisplay ref="infoDisplay" :name="name" :avatar-url="avatarUrl" :shumeiniang-image="shumeiniangImage"/>
</template>

<script>
import RecruitAnimation from './components/RecruitAnimation.vue'; 
import InfoDisplay from './components/InfoDisplay.vue';

const DIRECTORS = [
  {name: "林子煊", avatarUrl: "/avatar/azusa.jpeg", theme: "GenshinImpact", shumeiniangImage: "guitar2"},
  {name: "张家诚", avatarUrl: "/avatar/mugi.jpeg", theme: "Arknights", shumeiniangImage: "keyboard"},
  {name: "袁靖", avatarUrl: "/avatar/mio.jpeg", theme: "WutheringWaves", shumeiniangImage: "bass"},
  {name: "杨浩天", avatarUrl: "/avatar/ritsu.jpeg", theme: "PJSK", shumeiniangImage: "drum"},
  {name: "郭逸戈", avatarUrl: "/avatar/yui.jpeg", theme: "BanGDream", shumeiniangImage: "guitar1"}
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
      shumeiniangImage: ''
    }
  },
  methods: {
    displayLotteryAnim(name, avatarUrl, theme, shumeiniangImage) {
      const self = this;
      this.theme = theme;
      this.name = name;
      this.avatarUrl = avatarUrl;
      this.shumeiniangImage = shumeiniangImage;
      this.$nextTick(() => {
        this.$refs.infoDisplay.hide();
        this.$refs.bangLottery.play()
          .then(() => {
            self.$refs.infoDisplay.display();
          });
        }
      );
    },

    skipAnimation() {
      this.$refs.bangLottery.reset();
      this.$refs.infoDisplay.display();
    }
  },
  mounted() {
    document.addEventListener('click', () => {
      // this.displayLotteryAnim("林子煊", "/avatar/azusa.jpeg", "PJSK");
      // this.displayLotteryAnim("林子煊", "/avatar/azusa.jpeg", "WutheringWaves");
      // this.displayLotteryAnim("林子煊", "/avatar/azusa.jpeg", "Arknights");
      this.skipAnimation();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === "ArrowDown") {
        if (this.index + 1 >= DIRECTORS.length) return;
        this.index += 1;
        const director = DIRECTORS[this.index];
        this.displayLotteryAnim(director.name, director.avatarUrl, director.theme, director.shumeiniangImage);
      } else if (e.key === "ArrowUp") {
        if (this.index - 1 < 0) return;
        this.index -= 1;
        const director = DIRECTORS[this.index];
        this.displayLotteryAnim(director.name, director.avatarUrl, director.theme, director.shumeiniangImage);
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
