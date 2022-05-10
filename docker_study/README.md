2022/05/02 1일차
도커&쿠버네티스 라는 단어를 많이 들어봤다.
도대체 무엇일까? 도커부터 직접 공부해보자.

도커를 왜 쓸까?
- 어떤 프로그램을 다운 받는 과정을 간단하게 만들기 위해서 이다.

어떻길래 간단할까?
- 프로그램을 일반적으로 다운로드 받을경우, Installer 다운 - Installer 실행 - 설치완료의 과정이지만,
  이 과정에서 많은 에러가 발생할수 있다. Installer가 운영체제, 패키지버전, 서버 등 많은곳에서 영향을 받기 때문이다.
  예를들어 도커로 redis를 다운 받을경우 도커 클라이언트에서 docker run redis하면 손쉽게 받을수 있다.
  
도커는 무엇인가?
- 컨테이너를 사용하여 응용프로그램을 더 쉽게 만들고 배포하고 실행할 수 있도록 설계된 도구.
  컨테이너 기반의 오픈소스 가상화 플랫폼이며 생태계이다
  
컨테이너는 무엇인가?
- 다양한 프로그램, 실행환경을 컨테이너에 담아(추상화) 동일한 인터페이스를 제공하여 프로그램의 배포 및 관리를 단순하게 해준다.
  즉 코드와 모든 종속성을 패키지화 하여 응용프로그램이 다른 컴퓨팅 환경으로 빠르고 안정적으로 실행하게 해준다.
  https://www.docker.com/resources/what-container/ 
  
컨테이너 이미지란?
- 코드, 런타임, 시스템 도구, 라이브러리 및 설정과 같은 응용프로그램을 실행하는데 필요한 모든것을 포함하는
  가볍고 독립적으로 실행가능한 소프트웨어 패키지이다.
  도커 이미지를 이용해서 도커 컨테이너를 생성하고, 도커 컨테이너를 이용해서 프로그램을 실행한다.
  
도커 설치하기
- docker.com - get started - download for OS - Docker 사이트 회원가입 - hub.docker.com - Docker 로그인 - docker version
* Window Home은 Docker ToolBox or WSL 추가 필요.

도커의 흐름
- 도커Clinet(CLI)입력시 -> 도커 Server(Daemon)가 커맨드를 받아서 이미지생성, 컨테이너실행 과 같은 작업 수행
  ex) docker run hello-world -> 명령어를 도커 클라이언트가 도커 서버로 보내, 로컬에서 이미지Cache보관 장소에서 찾는다. 없을경우 도커 허브에서 가져온다.
 
하이퍼 바이저란?
- 호스트 시스템에서 다수의 게스트OS를 구동할수 있게 해주는 소프트웨어. 하드웨어와 각각의 VM을 모니터링 하는 중간관리자.
  VM마다 독립적으로 자원 할당. 논리적으로 분리되어 있어, 한쪽VM의 오류가 다른쪽으로 퍼지진 않음.
  
도커와 기존VM의 차이점
- 도커 컨테이너는 하이퍼 바이저와 게스트OS가 필요하지 않으므로 오버헤드가 적어 더 가볍다.
  도커는 호스트OS위에 어플리케이션의 실행 피키지인 이미지를 배포. -> 같은 호소트, 다른 컨테이너와 동일한 커널을 공유. (도커엔진과 하이퍼바이저가 유사)
  
리눅스에서 사용되는 Cgroup 과 nameSpace
- 컨테이너와 호스트에서 실행되는 다른 프로세스 사이 벽을 만드는 리눅스 커널 기능들.

Cgroup
- cpu,메모리, network, HD i/o등 프로세스 그룹의 시스템 리소스 사용량을 관리
  어떤 어플리케이션이 사용량이 많으면 그 어플을 Cgroup에 넣어 cpu와 메모리 사용 제한 가능.
  
nameSpace
- 하나의 시스템에서 프로세스를 격리시킬 수 있는 가상화 기술.
  별개의 독립된 공간을 사용하는 것처럼 격리된 환경 제공.
  
위의 둘은 리눅스에서 사용된다고 했는데 난 윈도우 인데 어떻게 도커에서 사용되나?
- docker Clinet 에서 docker version입력. 도커 서버의OS가 리눅스 인것을 볼수 있다. 그렇기에 리눅스 커널을 사용하여 Cgroup및 nameSpace사용!
  
어떻게 도커 이미지가 컨테이너로 만들어 질까?
- 이미지는 응용 프로그램을 실행하는데 필요한 모든것을 포함하고 있다.
  필요한 모든것은 시작시 실행될 명령어(run appName), 파일 스냅샷(디렉토리나 파일을 카피 한것)
  
이미지로 컨테이너를 만드는 순서
- 1. Docker 클라이언트에 docker run Image 입력시
  2. 도커 이미지에 있는 파일 스냅샷을 컨테이너 하드 디스크에 옮겨 준다.
  3. 이미지에서 가지고 있는 명령어(컨테이너가 실행될때 사용될 명령어)를 이용해 해당app을 실행시킨다.

05/03 2일차
작동 순서 복습.
- docker run 이미지이름 명령어 -> 도커 클라이언트 언급 / 컨테이너 생성 및 실행 / 이 컨테이너를 위한 이미지 / 이 자리는 이미지가 가지고 있는 시작명령어를 무시하고 커맨드 실행시킴.


도커 명령어 및 생명주기
- docker ps (-a) -> docker process status 현재 도커컨테이너의 상태. (all)
- docker create 이미지 이름 -> 파일 스냅샷을 컨테이너 생성후 하드디스크로 옮김. 컨테이너 ID생성
- docker start 컨테이너ID/이름 -> 시작시 실행될 명령어 run이 실행됨.
- docker run -> 위의 두 가지 작업이 한번에 되는것.
- docker stop 컨테이너ID/이름 -> docker stop -> SIGTERM (Grace period.정리하는시간) -> SIGKILL -> Main Process
- docker kill 컨테이너ID/이름 -> docker kill ->         (Grace Period x 즉시멈춤)    SIGKILL -> Main Process
- docker rm ID/이름 (or `docker ps -a -q`) -> 중지된 컨테이너 삭제.
- docker rmi 이미지ID -> 이미지 삭제
- docker system prune -> 한번에 컨테이너, 이미지, 네트워크 모두 삭제. 도커를 쓰지 않을때 모두 정리할때 사용. 단, 실행중인 컨테이너에 영향x
- docker exeu 컨테이너ID 명령어 -> 이미 실행중인 컨테이너에 명령어 실행. run은 새 컨테이너를 만들고 실행. 
ex) redis서버를 실행후, redis-cli를 실행하면, 컨테이너 밖에서 명령어가 실행되므로 작동하지 않는다.
    이때 exce로 컨테이너 안에 들어가서 명령어를 주어야 한다. - docker it 컨테이너ID redis-cli -> redis-cli접속
	-it -> interactive terminal. 명령어 실행후 계속 명령어 입력가능. -it가 없다면 redis-cli만 실행후 밖으로 나와버림.
- docker exeu -it 컨테이너ID sh -> 컨테이너 안에서 shell환경으로 직접 들어가 입력가능. 매번 docker~ 입력 불필요.(sh bash powershell...)

지금까지는 도커서버에 있는 도커 이미지를 사용했다. 도커이미지를 직접 만들어보자.
- Docker file작성 -> 도커클라이언트 전달 -> 도커서버 -> 이미지 생성
  Docker file은 도커이미지를 만들기 위한 설정파일. 컨테이너가 어떻게 행동해야 하는지에 대한 설정정의.
  Docker client 전달 후 도커서버에서 전달된 모든 중요한 작업을 한다.
  - dockerfile 폴더 참고.
  
베이스 이미지란?
- 도커 이미지는 여러개의 레이어로 되어 있다. 그중 이 이미지의 기반이 되는 부분이다. OS에 대한 정보가 들어있다.

WSL2에 설치된 Linux에서 Dockerfile 빌드시 step등 정보가 terminal에 온전히 보이지 않을때
- buildkit 이 기존 도커엔진에서 제공하는 기능을 대채하여 발생.
  도커 빌드전, DOCKER_BUILDKIT=0으로 Disable 시켜 빌드 실행.
  또는 도커엔진의 설정에서 buildkit : false 로 변경
  
이미지를 만들때
- 베이스 이미지를 먼저 임시 컨테이너에 넣은후, 그 임시 컨테이너를 토대로 새로운 이미지가 생성된다. 임시 컨테이너는 삭제된다.
  이미지 -> 임시컨테이너(새로운 명령어, 파일스냅샷추가) -> 새로운 이미지
  그렇기 떄문에 이미지ID가 만들어지고 지워지며, 새로운 이미지의ID가 최종.
  
도커 이미지에 이름 주는 방법.
- docker build <-t 나의도커아이디 / 저장소/프로젝트이름 : 버전> ./
  ex) docker build -t ajw9491/hello:latest ./ -> 도커이미지명으로 ajw9491/hello:latest 사용가능
 
05/04 3일차
도커 빌드시
- 종속성을 설치하기 위해선 해당 베이지 이미지가 그 종속성을 설치할수 있는 파일을 갖고 있어야 한다.
  ex) RUN npm install을 위해선 FROM node 를 사용하여야함.
- 임시 컨테이너에서는 외부파일을 함께 빌드하지 않으므로, COPY ./ ./를 입력하여 함께 빌드한다.

도커 빌드하여 이미지파일을 실행시켰는데 왜 로컬에서 접속이 안되나?
- 네트워크도 위 처럼 로컬 네트워크에 있던것을 컨테이너 내부에 있는 네트워크에 연결시켜야 한다.
  옵션 -p 5000 : 8080 -> -port 로컬port번호 : 컨테이너port번호 
  로컬 포트번호와 컨테이너 포트번호를 맵핑하여, 로컬포트5000으로 접속시 컨테이너속 8080으로 접속한다.
  ex) docker run -p 5000:8080 ajw9491/nodejs

workdir을 설정해야 하는 이유.
- workdir가 없이 build하게 될 경우, 모든 소스파일이 rootdir에 모이게 된다.
  이는 소스파일이 많을경우 관리가 힘들어 지며, 같은 이름의 파일이 존재할 경우 덮어쓰여진다.
  WORKDIR /usr/src/app 을 예시로 주면, docker run실행시 하위 디렉토리 부터 접근이 된다.
  rootdir에 home, bin, dev 파일이, /usr 에는 src, /app 에는 .json, Dockerfile 등등 
  쉘로 접속하여 ls, cd / 루트디렉토리로 접속하여 확인한다.
  
어플리케이션 소스변경으로 재빌드시, 효율적으로 하기
- 변경된소스를 재빌드시, 종속성을 제외하고 빌드가 가능하다.
  package.json과 같은 파일은 수정이 되지 않는한
  다시 받을 필요가 없기 떄문에 기존에 빌드된 캐시를 그대로 사용하는게 효율적이다.
  ex)RUN 실행전, COPY에 package.json ./ 을 추가하고, 기존 COPY를 RUN아래로 내린다. 
     콘솔에서 도커 로그를 보면, --->Using cache로, 캐시를 이용해 빠르게 빌드된다.
  -하지만 이마저도, 소스를 변경할때마다 변경된 소스부분을COPY한후 이미지를 다시 빌드하고 컨테이너를
   다시실행해줘야지 변경된 소스가 화면에 반영된다. 이미지를 매번 새로 빌드하게 되므로 작업시간이 크다.

Docker Volume이란?
- 도커 컨에티너에서 Docker Volume을 이용하여 
  기존의 COPY가 아닌 로컬에 있는파일을 Mapping하는것이다. 
  ex) docker run -p 5000:8080 -v /usr/src/app/node_modules -v $(pwd):/usr/src/app imageId 
      맥$(pwd) => 윈도우%cd% powerShell ${pwd}
	  
5/5 4일차
Redis란?
- Remote Dictionary Server로, 메모리 기반의 키-값 구조
  데이터 관리 시스템. 모든 데이터를 메모리에 저장하고 빠르게 조회할수 있는 비관계형 데이터베이스(NoSql)
  
Redis를 왜 쓰는건가?
- 메모리에 저장하기 때문에 기존RDBMS에 비해 조회가 빠르며, 메모리에 저장하지만 영속적으로 보관가능.
  서버 재부팅해도 데이터 유지.
  
도커 환경에서 레디스 클라이언트 생성시 주의사항.
- 도커를 사용하지 않는 환경은 레디스 서버가 작동되고있는 곳의 host옵션을 url로 주지만,
  도커 Compose를 사용할때는 host옵션을 docker-compose.yml 파일에 명시한 컨테이너 이름으로 준다.
	  
컨테이너 작동순서
- 레디스 클라이언트가 작동하려면 레디스 서버가 켜져 있어야 한다.
  레디스 서버를 위한 컨테이너를 먼저 실행하고, 노드js를 위한 컨테이너를 실행한다.
  docker run redis - 레디스 서버 실행
  docker build -t ajw9491/docker-dompose-app ./ nodejs파일 이미지 생성
  docker run ajw9491/docker-dompose-app
- 서로 다른 컨테이너는 설정없이 접근이 불가능 하여 에러가 난다.
  이때, 멀티 컨테이너 상황에서 쉽게 네트워크를 연결 시켜주기 위해 Docker Compose를 사용한다.
 
docker-compose.yml작성
 -yaml yml 파일은 XML,json처럼 데이터 형식 포맷이며, 좀 더 사람이 읽기 쉬운 포맷이다.
 -docker-compose.yml 파일 주석 참고.
 -docker-compose up 로 실행.
 
5/6 5일차
  2시간동안 헤맸던 나.
- redis 4.0.1버전에서 host프로퍼티 부분이 바뀌어, 오류가남. 우선 3.0.1버전 사용하자.
- (root) Additional property node-app is not allowed
   .yml 파일에서 띄어쓰기는 매우 중요하다. 이 부분이 맞지 않을경우 발생
- node.js express api 에서 res.send([body])의 인자값으론, Buffer obj, String, Array
  만 보낼수 있다. Integer 값을 보내면 오류가 난다.
  

5/7 6일차
- docker-compose down 종료
- docker-compose up <d> 이미지가 없을때 이미지를 빌드하고 컨테이너 시작 <detached모드. 앱을 백그라운드에서 실행>
- docker-compose up --build 이미지가 있든없든 이미지를 빌드하고 컨테이너 시작
 
간단한 어플을 실제로 배포해보기.
리액트 설치
- npx create-react-app ./ 현재 디렉토리에 리액트 설치
   현재node.js버전에서 지원하지 않아, 14버전 이상으로 업데이트하라고 오류메세지가 출력됬지만,
   node.js를 지워도, 재설치해도, 업데이트해도 12.x버전이 출력됬다. where node를 입력하니
   graalvm안에 node.cmd가 찍혔다. 가보니 graalvm이 node.js runtime도 같이 설치가 된것 같다
   nodejs를 삭제후 재설치해도, 해당버전이 반영이 안된다. 혹시나 하고 nodejs환경변수를 graalvm위로 올렸다.
   node -v 실행시, 최신버전node가 먼저 실행된다. npm까지 정상적으로 버전업데이트가 되었다.  -80분 소요ㅠㅠ
 
 5/9 7일차
리액트 실행 명령어
- npm run start 리액트 실행
- npm run test 개발 완료후 테스트.
- npm run build 테스트 완료 후 배포파일 생성

도커를 이용하여 개발단계에서 리택트 실행
- 현재까지는 Dockerfile을 하나만 만들었지만, 실제로는 개발단계과 실제 배포용 파일을 딷로 만든다.
  개발환경과 실제 환경에서도 다르게 해줘야 하는 부분이 있기때문. 개발단게에선 Dockerfile.dev를 우선 만든다.

docker build시 unable to evaluate symlink .. 에러
- 이미지 빌드시, 해당 디렉토리만 지정해주면 dockerfile을 자동으로 찾아서 빌드 하지만, 현재 도커파일을 개발용인 dockerfile.dev로 만들었기에
  dockerfile을찾지 못하여 발생. build시 임의로 참조할 파일을 알려줘야 한다.
- docker build -f Dockerfile.dev . -> -f 옵션은 이미지를 빌드할때 쓰일 도커파일을 지정.

도커를 이용한 리액트 앱에서 테스트 진행
- 기존 npm run test -> modules가 한번더 copy되므로 삭제하였다. 
- docker run 이미지이름 npm run test -> 도커 환경에서 리액트 엡 테스트.
- test파일도 수정될경우, 즉시 반영될수 있도록 yml에 추가한다.

개발환경 서버와 운영환경 서버를 왜 다르게 사용하나?
- 개발에서 사용하는 서버는 소스를 변경시 자동으로 전체 앱을 다시 빌드해서 변경 소스를 반영해주는 것 같이 개발환경에 특화된 기능들이 있기에
  그러한 기능이 없는 Nginx서버보다 더욱 적합하다.
  운영환경은 개발에 필요한 기능들이 필요하지 않기에 Apache보다 단순하고, 깔끔한 동시접속처리에 특화된 Nginx를 사용한다.
  
운영환경을 위한 Dockerfile은 2단계로 이루어져 있다.
- 1. 첫번째 단계는 빌드 파일들을 생성한다. (Builder Stage)
- 2. 두번째 단계는 Nginx를 가동하고 첫번째 단계에서 생성된 빌드폴더의 파일들을 웹 브라우저의 요청에 따라 제공하여 준다. (Run Stage)

5/10 8일차
Nginx의 기본포트는 30번 이므로, Mapping시 30번 port를 매핑한다.
새로 빌드 할 때 이름을 지정하지 않으면, 이전에 빌드된 ID의 이미지를 실행시킨다.

github에 올린후, Travis CI에서 이 소스가 잘 작성된 코드인지 확인하기.
Travis CI란?
- github에서 제공하는 오픈소스 프로젝트로, Travis CI를 이용하여 github에 있는 repository에 있는 프로젝트를
  특정 이벤트에 따라 자동으로 테스트, 빌드하거나 배포할수 있다. 단, Private repository는 유료. Public repository는 10000크레딧 무료
  
CI란?
- Continuous Integration, 지속적 통합. 팀의 구성원들이 작업한 내용을 지속적으로 통합하여 품질 관리를 적용하는 프로세스.

CI시스템을 구축하지 않으면?
- 개발자들이 각자 개발한 소스코드를 형상관리 서버에 커밋하면, 별도의 품질관리를 거치지 않고 대부분 개발이 끝난 막바지에 통합을 하여 테스트를 진행하게 된다.
  이경우, 개발중 별도의 품질 관리를 수행하지 않았기에 잘못된 소스코드를 형상관리 시스템에 반영하였을 경우 발생되는 문제가 개발 후반에 장애로 발견된다.
  CI시스템을 구축하게 되면 CI서버는 형상관리 서버에 Commit된 소스를 주기적으로 Polling하여 컴파일, 단위테스트 등 테스트 과정을 수행하며
  신규 또는 수정된 소스코드가 결함이 있는지 여부를 지속적으로 검증한다. 검증 결과는 이메일, RSS등의 피드백 매커니즘을 통해 개발자로 전달되고,
  이를 통해 조기에 결함을 발견하여 해결할수 있는것이다.

Travis CI의 flow
- 로컬Git -> Github -> Travis CI -> AWS
- 1. 로컬git소스를 github 저장소에 push
- 2. github master 저장소에 소스가 push되면 Travis CI에게 소스가 push되었다고 알림.
- 3. Travis CI는 업데이트 된 소스를 Github에서 가지고옴.
- 4. github에서 가져온 소스의 테스트코드 실행
- 5. 성공하면 AWS같은 호스팅 사이트로 보내어 배포