<template>
  <div>
    <h2 class="MainText">카카오맵</h2>

    <div class="container">
      <div id="placesList" class="list-overlay"></div>
      <div id="map"></div>
    </div>

    <div class="input">
      <div class="input-group mb-3">
        <input
          type="text"
          class="form-control"
          placeholder="도시 또는 은행 입력"
          v-model="searchQuery"
          @keyup.enter="searchPlaces"
        />
        <button class="btn btn-primary" @click="searchPlaces">검색</button>
      </div>
    </div>
  </div>
</template>

<script>
const API_KEY = import.meta.env.VITE_API_KEY;

export default {
  name: "KakaoMap",
  mounted() {
    let script = document.createElement("script");
    script.type = "text/javascript";
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${API_KEY}&autoload=false&libraries=services,clusterer,drawing`;

    // 카카오맵 API 스크립트 로드

    document.head.appendChild(script);

    script.onload = () => {
      kakao.maps.load(
        function () {
          // Inside this callback, the SDK is guaranteed to be loaded
          this.loadKakaoMap();
        }.bind(this)
      );
    };
  },
  data() {
    return {
      searchQuery: "",
      map: null,
      infowindow: null,
      markers: [],
    };
  },

  methods: {
    loadKakaoMap() {
      let mapContainer = document.getElementById("map");
      let mapOption = {
        center: new kakao.maps.LatLng(37.5013, 127.0397),
        level: 3,
      };

      this.map = new kakao.maps.Map(mapContainer, mapOption);
      this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
      this.searchPlaces();
      // this.addMarker();
    },
    getListItem(index, place) {
      var el = document.createElement("li"),
        itemStr =
          '<span class="markerbg marker_' +
          (index + 1) +
          '"></span>' +
          '<div class="info">' +
          "   <h5>" +
          place.place_name +
          "</h5>";

      if (place.road_address_name) {
        itemStr +=
          "    <span>" +
          place.road_address_name +
          "</span>" +
          '   <span class="jibun gray">' +
          place.address_name +
          "</span>";
      } else {
        itemStr += "    <span>" + place.address_name + "</span>";
      }

      itemStr += '  <span class="tel">' + place.phone + "</span>" + "</div>";

      el.innerHTML = itemStr;
      el.className = "item";

      return el;
    },
    searchPlaces() {
      const ps = new kakao.maps.services.Places(this.map);
      const options = {
        category_group_code: "BK9",
      };

      ps.keywordSearch(
        this.searchQuery,
        (data, status) => {
          console.log(data);
          if (status === kakao.maps.services.Status.OK) {
            const banks = data.filter(
              (place) => place.category_group_code === "BK9"
            );
            this.clearMarkers();
            this.displayMarkers(banks);
          } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
            alert("검색 결과가 존재하지 않습니다");
            return;
          } else if (status === kakao.maps.services.Status.ERROR) {
            alert("검색 결과 중 오류가 발생했습니다.");
            return;
          }
        },
        options
      );
    },
    clearMarkers() {
      if (this.markers) {
        this.markers.forEach((marker) => {
          marker.setMap(null);
        });
        this.markers = [];
      }
    },
    showInfowindowOnMarker(marker, place) {
      let content = `<div style="padding: 5px; font-size: 12px;">${place.place_name}</div>`;
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    displayMarkers(places) {
      this.clearMarkers();
      if (places.length > 0) {
        let listEl = document.getElementById("placesList");
        listEl.innerHTML = "";
        let bounds = new kakao.maps.LatLngBounds();

        places.forEach((place, index) => {
          let marker = new kakao.maps.Marker({
            map: this.map,
            position: new kakao.maps.LatLng(place.y, place.x),
          });

          this.markers.push(marker);

          kakao.maps.event.addListener(marker, "mouseover", () => {
            this.infowindow.setContent(
              '<div style="padding:5px;font-size:12px;">' +
                place.place_name +
                "</div>"
            );
            this.infowindow.open(this.map, marker);
          });

          kakao.maps.event.addListener(marker, "mouseout", () => {
            this.infowindow.close();
          });

          // 목록 추가
          let listItem = this.getListItem(index, place);
          listItem.addEventListener("mouseover", () => {
            this.showInfowindowOnMarker(marker, place);
          });
          listItem.addEventListener("mouseout", () => {
            this.infowindow.close();
          });
          console.log(listItem);
          listEl.appendChild(listItem);
          console.log(listEl);

          // 지도 영역 설정
          bounds.extend(new kakao.maps.LatLng(place.y, place.x));
        });
        this.map.setBounds(bounds);
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  position: relative;
}

.input {
  display: flex;
  justify-content: center;
  width: 300px;
  margin: 50px auto;
}

#map {
  /* margin: 50px auto; */
  width: 100%;
  height: 400px;
  position: relative;
  z-index: 0;
}

#placesList {
  position: absolute;
  top: 0;
  left: 0;
  width: 30%;
  max-height: 400px;
  overflow-y: auto;
  background-color: rgba(255, 255, 255, 0.8);
  /* Adjust transparency as needed */
  padding: 10px;
  z-index: 1;
  /* Ensure the list is above the map */
  /* width: 300px;
  max-height: 500px;
  overflow-y: auto;
  margin: 10px 0; Adjust the margin based on your layout */
}

.list-overlay {
  z-index: 1;
}

.MainText {
  text-align: center;
}
</style>
